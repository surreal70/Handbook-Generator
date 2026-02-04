"""
CLI Interface for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, Tuple

from src.template_manager import TemplateManager
from src.config_manager import ConfigManager
from src.placeholder_processor import PlaceholderProcessor
from src.data_source_adapter import DataSourceAdapter
from src.netbox_adapter import NetBoxAdapter
from src.meta_adapter import MetaAdapter
from src.output_generator import OutputGenerator
from src.logger import HandbookLogger, StatisticsCalculator


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        prog='handbook-generator',
        description='Generate professional handbooks from markdown templates with data integration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python -m src.cli
  
  # Generate German backup handbook in both formats
  python -m src.cli --language de --template backup
  
  # Generate English ISMS handbook in PDF only
  python -m src.cli -l en -t isms -o pdf
  
  # Generate German BCM handbook in both formats
  python -m src.cli -l de -t bcm
  
  # Generate English BSI Grundschutz handbook in Markdown only
  python -m src.cli -l en -t bsi-grundschutz -o markdown
  
  # Verbose mode with custom config
  python -m src.cli -l de -t bcm -v -c custom_config.yaml
        """
    )
    
    parser.add_argument(
        '--language', '-l',
        type=str,
        choices=['de', 'en'],
        help='Language for handbook generation (de=German, en=English)'
    )
    
    parser.add_argument(
        '--template', '-t',
        type=str,
        choices=['backup', 'bcm', 'bsi-grundschutz', 'isms', 'it-operation'],
        help='Template type/category for handbook (backup=Backup procedures, bcm=Business Continuity Management, bsi-grundschutz=BSI IT-Grundschutz, isms=Information Security Management System, it-operation=IT Operations)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        choices=['markdown', 'pdf', 'both'],
        default='both',
        help='Output format (default: both)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging with detailed placeholder replacements'
    )
    
    parser.add_argument(
        '--config', '-c',
        type=str,
        default='config.yaml',
        help='Path to configuration file (default: config.yaml)'
    )
    
    parser.add_argument(
        '--create-config',
        action='store_true',
        help='Create default configuration file and exit'
    )
    
    parser.add_argument(
        '--template-dir',
        type=str,
        default='templates',
        help='Path to templates directory (default: templates)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='Handbook',
        help='Path to output directory (default: Handbook)'
    )
    
    return parser.parse_args()


def validate_arguments(args: argparse.Namespace) -> Optional[str]:
    """
    Validate parsed arguments for consistency.
    
    Args:
        args: Parsed arguments namespace
        
    Returns:
        Error message if validation fails, None if valid
    """
    # If --create-config is set, no other validation needed
    if args.create_config:
        return None
    
    # Both language and template must be provided together or both omitted
    if (args.language is None) != (args.template is None):
        return (
            "Error: --language and --template must be provided together, "
            "or both omitted for interactive mode."
        )
    
    return None


def interactive_selection(template_manager: TemplateManager) -> Tuple[str, str]:
    """
    Interactive language and template type selection.
    
    Args:
        template_manager: TemplateManager instance for discovering available templates
        
    Returns:
        Tuple of (language, template_type)
        
    Raises:
        SystemExit: If no templates are available or user cancels
    """
    # Discover available templates
    discovered = template_manager.discover_templates()
    
    if not discovered:
        print("ERROR: No templates found in template directory.", file=sys.stderr)
        print(f"Expected structure: {template_manager.template_root}/{{language}}/{{category}}/", 
              file=sys.stderr)
        sys.exit(1)
    
    # Display available options
    print("\n" + "=" * 60)
    print("Available Templates")
    print("=" * 60)
    
    for language, categories in sorted(discovered.items()):
        print(f"\nLanguage: {language}")
        for category, templates in sorted(categories.items()):
            template_count = len(templates)
            print(f"  - {category}: {template_count} template(s)")
    
    print("=" * 60)
    
    # Get language selection
    available_languages = sorted(discovered.keys())
    while True:
        language_input = input(f"\nSelect language ({'/'.join(available_languages)}): ").strip().lower()
        if language_input in available_languages:
            language = language_input
            break
        print(f"Invalid language. Please choose from: {', '.join(available_languages)}")
    
    # Get template type selection
    available_types = sorted(discovered[language].keys())
    while True:
        type_input = input(f"Select template type ({'/'.join(available_types)}): ").strip().lower()
        if type_input in available_types:
            template_type = type_input
            break
        print(f"Invalid template type. Please choose from: {', '.join(available_types)}")
    
    return language, template_type


def main() -> int:
    """
    Entry point for the handbook generator.
    
    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    # Parse arguments
    args = parse_arguments()
    
    # Validate arguments
    validation_error = validate_arguments(args)
    if validation_error:
        print(validation_error, file=sys.stderr)
        return 1
    
    # Initialize logger
    logger = HandbookLogger(verbose=args.verbose)
    
    # Handle --create-config
    if args.create_config:
        config_path = Path(args.config)
        config_manager = ConfigManager(config_path)
        try:
            config_manager.create_default_config()
            logger.log_info(f"✓ Default configuration file created: {config_path}")
            logger.log_info("Please edit the configuration file with your credentials before running the generator.")
            return 0
        except FileExistsError as e:
            logger.log_error(str(e))
            return 1
        except Exception as e:
            logger.log_error(f"Failed to create configuration file: {str(e)}")
            return 1
    
    # Load configuration
    config_path = Path(args.config)
    config_manager = ConfigManager(config_path)
    
    try:
        config = config_manager.load_config()
        logger.log_verbose(f"Configuration loaded from: {config_path}")
    except FileNotFoundError as e:
        logger.log_error(str(e))
        return 1
    except Exception as e:
        logger.log_error(f"Failed to load configuration: {str(e)}")
        return 1
    
    # Initialize template manager
    template_root = Path(args.template_dir)
    template_manager = TemplateManager(template_root)
    
    # Validate template structure
    structure_warnings = template_manager.validate_template_structure()
    for warning in structure_warnings:
        logger.log_warning(warning)
    
    # If structure validation failed critically, exit
    if structure_warnings and "not found" in structure_warnings[0].lower():
        return 1
    
    # Determine language and template type
    if args.language and args.template:
        language = args.language
        template_type = args.template
        logger.log_verbose(f"Using command-line parameters: language={language}, template={template_type}")
    else:
        # Interactive mode
        try:
            language, template_type = interactive_selection(template_manager)
        except (KeyboardInterrupt, EOFError):
            print("\n\nOperation cancelled by user.")
            return 1
    
    # Verify selected combination exists
    try:
        templates = template_manager.get_templates(language, template_type)
    except ValueError as e:
        logger.log_error(str(e))
        return 1
        
    if not templates:
        logger.log_error(
            f"No templates found for language '{language}' and type '{template_type}'. "
            f"Please check your template directory structure."
        )
        return 1
    
    logger.log_info(f"\n✓ Found {len(templates)} template(s) for {language}/{template_type}")
    
    # Initialize data source adapters
    data_sources = {}
    
    # Add meta adapter if metadata is available
    if config.metadata:
        try:
            meta_adapter = MetaAdapter(config.metadata)
            if meta_adapter.connect():
                data_sources['meta'] = meta_adapter
                logger.log_verbose("✓ Meta adapter initialized with organization metadata")
            else:
                logger.log_warning("Failed to initialize meta adapter")
        except Exception as e:
            logger.log_warning(f"Meta adapter initialization failed: {str(e)}")
    
    # Add NetBox adapter if configured
    if config.netbox_url and config.netbox_api_token:
        try:
            netbox_adapter = NetBoxAdapter(config.netbox_url, config.netbox_api_token)
            if netbox_adapter.connect():
                data_sources['netbox'] = netbox_adapter
                logger.log_verbose("✓ Connected to NetBox data source")
            else:
                logger.log_warning("Failed to connect to NetBox - placeholder replacement may be limited")
        except Exception as e:
            logger.log_warning(f"NetBox adapter initialization failed: {str(e)}")
    
    # Initialize placeholder processor
    processor = PlaceholderProcessor(data_sources)
    
    # Initialize output generator
    output_dir = Path(args.output_dir)
    output_generator = OutputGenerator(output_dir)
    
    # Start processing
    logger.start_processing()
    logger.log_info("\nProcessing templates...")
    
    # Process all templates
    processed_results = []
    processed_contents = []
    all_warnings = []
    all_errors = []
    
    for template in templates:
        logger.log_processing(template.path.name)
        
        # Read template content
        try:
            content = template.read_content()
        except Exception as e:
            error_msg = f"Failed to read template {template.path.name}: {str(e)}"
            logger.log_error(error_msg)
            all_errors.append(error_msg)
            continue
        
        # Process template
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
        processed_contents.append(result.content)
        
        # Log replacements in verbose mode
        for replacement in result.replacements:
            logger.log_replacement(replacement)
        logger.log_replacements_summary(result.replacements, template.path.name)
        
        # Collect warnings and errors
        all_warnings.extend(result.warnings)
        all_errors.extend(result.errors)
    
    # Generate output
    logger.log_info("\nGenerating output...")
    
    output_format = args.output
    markdown_path = None
    pdf_path = None
    
    # Generate markdown
    if output_format in ['markdown', 'both']:
        md_result = output_generator.generate_markdown(
            processed_contents,
            language,
            template_type
        )
        all_warnings.extend(md_result.warnings)
        all_errors.extend(md_result.errors)
        
        if md_result.markdown_path:
            markdown_path = md_result.markdown_path
            logger.log_info(f"✓ Markdown generated: {markdown_path}")
    
    # Generate PDF
    if output_format in ['pdf', 'both']:
        assembled_content = output_generator.assemble_markdown(processed_contents)
        pdf_result = output_generator.generate_pdf(
            assembled_content,
            language,
            template_type
        )
        all_warnings.extend(pdf_result.warnings)
        all_errors.extend(pdf_result.errors)
        
        if pdf_result.pdf_path:
            pdf_path = pdf_result.pdf_path
            logger.log_info(f"✓ PDF generated: {pdf_path}")
    
    # Calculate statistics
    processing_time = logger.get_elapsed_time()
    assembled_content = output_generator.assemble_markdown(processed_contents)
    
    output_size = 0
    if markdown_path and markdown_path.exists():
        output_size += markdown_path.stat().st_size
    if pdf_path and pdf_path.exists():
        output_size += pdf_path.stat().st_size
    
    stats = StatisticsCalculator.calculate_statistics(
        processed_results,
        assembled_content,
        output_size,
        processing_time
    )
    
    # Log statistics
    logger.log_statistics(stats)
    
    # Log summary of warnings and errors
    logger.log_summary(all_warnings, all_errors)
    
    # Disconnect data sources
    for adapter in data_sources.values():
        try:
            adapter.disconnect()
        except Exception:
            pass  # Ignore disconnect errors
    
    # Return appropriate exit code
    if all_errors:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
