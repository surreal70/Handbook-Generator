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
from src.netbox_metadata_loader import NetBoxMetadataLoader
from src.output_generator import OutputGenerator
from src.html_output_generator import HTMLOutputGenerator
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
  # Interactive mode (test mode required)
  python -m src.cli --test
  
  # Generate German BCM handbook in both formats (markdown + PDF)
  python -m src.cli --language de --template bcm --test
  
  # Generate English ISMS handbook in PDF only
  python -m src.cli -l en -t isms -o pdf --test
  
  # Generate German BCM handbook in HTML format
  python -m src.cli -l de -t bcm -o html --test
  
  # Generate English BSI Grundschutz handbook in all formats
  python -m src.cli -l en -t bsi-grundschutz -o all --test
  
  # Generate German IDW PS 951 IT Auditing handbook
  python -m src.cli -l de -t idw-ps-951 --test
  
  # Generate English NIST CSF 2.0 handbook
  python -m src.cli -l en -t nist-csf -o pdf --test
  
  # Generate German TOGAF Enterprise Architecture handbook
  python -m src.cli -l de -t togaf -o html --test
  
  # Generate English ISO/IEC 38500 IT Governance handbook
  python -m src.cli -l en -t iso-38500 --test
  
  # Generate German ISO 31000 Risk Management handbook
  python -m src.cli -l de -t iso-31000 -o pdf --test
  
  # Generate English CSA CCM Cloud Security handbook
  python -m src.cli -l en -t csa-ccm -o html --test
  
  # Generate German TISAX Automotive Security handbook
  python -m src.cli -l de -t tisax --test
  
  # Generate English SOC 1 / SSAE 18 handbook
  python -m src.cli -l en -t soc1 -o pdf --test
  
  # Generate German COSO Internal Control handbook
  python -m src.cli -l de -t coso --test
  
  # Generate English DORA DevOps Metrics handbook
  python -m src.cli -l en -t dora -o html --test
  
  # Generate separate markdown files for each template
  python -m src.cli -l de -t bcm --test --separate-files
  
  # Generate PDF with table of contents and page breaks
  python -m src.cli -l de -t isms -o pdf --test --pdf-toc
  
  # Generate both separate markdown files and PDF with TOC
  python -m src.cli -l de -t bcm --test --separate-files --pdf-toc
  
  # Verbose mode with custom config
  python -m src.cli -l de -t bcm -v -c custom_config.yaml --test
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
        choices=['bcm', 'bsi-grundschutz', 'cis-controls', 'common-criteria', 'coso', 'csa-ccm', 'dora', 'email-service', 'gdpr', 'hipaa', 'idw-ps-951', 'isms', 'iso-31000', 'iso-38500', 'iso-9001', 'it-operation', 'nist-800-53', 'nist-csf', 'pci-dss', 'service-templates', 'soc1', 'tisax', 'togaf', 'tsc'],
        help='Template type/category for handbook (bcm=Business Continuity Management, bsi-grundschutz=BSI IT-Grundschutz, cis-controls=CIS Controls v8 Hardening, common-criteria=Common Criteria EAL, coso=COSO Internal Control Framework, csa-ccm=Cloud Security Alliance CCM, dora=DORA DevOps Metrics, email-service=Email Service Management, gdpr=GDPR Compliance, hipaa=HIPAA Compliance, idw-ps-951=IDW PS 951 IT Auditing, isms=Information Security Management System, iso-31000=ISO 31000 Risk Management, iso-38500=ISO/IEC 38500 IT Governance, iso-9001=ISO 9001 Quality Management, it-operation=IT Operations, nist-800-53=NIST 800-53 Security Controls, nist-csf=NIST Cybersecurity Framework 2.0, pci-dss=PCI-DSS Payment Card Security, service-templates=Service Management Templates, soc1=SOC 1 / SSAE 18, tisax=TISAX Automotive Security, togaf=TOGAF Enterprise Architecture, tsc=Trust Services Criteria SOC2)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        choices=['markdown', 'pdf', 'html', 'both', 'all'],
        default='both',
        help='Output format: markdown (single or separate files), pdf (with or without TOC), html (mini-website), both (markdown+pdf), or all (markdown+pdf+html) (default: both)'
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
    
    parser.add_argument(
        '--test',
        action='store_true',
        help='Enable test mode to allow output generation (required for safety)'
    )
    
    parser.add_argument(
        '--separate-files',
        action='store_true',
        help='Generate separate markdown files for each template instead of a combined file (creates TOC.md with links)'
    )
    
    parser.add_argument(
        '--pdf-toc',
        action='store_true',
        help='Generate PDF with table of contents and page breaks between templates (improves navigation and readability)'
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
    
    # Load NetBox metadata if NetBox is configured
    metadata_netbox_path = Path("metadata-netbox.yaml")
    if config.netbox_url and config.netbox_api_token:
        logger.log_info("\nLoading NetBox metadata...")
        try:
            # Get role distinction configuration
            role_config = config.netbox_role_distinction or {
                'method': 'field',
                'field': 'role',
                'mappings': {}
            }
            
            # Initialize NetBox metadata loader
            netbox_loader = NetBoxMetadataLoader(
                config.netbox_url,
                config.netbox_api_token,
                role_config
            )
            
            # Load metadata from NetBox
            netbox_metadata = netbox_loader.load_metadata()
            
            # Save to metadata-netbox.yaml
            netbox_loader.save_to_yaml(netbox_metadata, str(metadata_netbox_path))
            
            logger.log_verbose(f"✓ NetBox metadata loaded and saved to {metadata_netbox_path}")
            
        except ConnectionError as e:
            logger.log_warning(f"Failed to load NetBox metadata: {str(e)}")
            logger.log_warning("Continuing without NetBox metadata...")
        except Exception as e:
            logger.log_warning(f"Unexpected error loading NetBox metadata: {str(e)}")
            logger.log_warning("Continuing without NetBox metadata...")
    
    # Initialize data source adapters
    data_sources = {}
    
    # Add meta adapter if metadata is available
    if config.metadata:
        try:
            meta_adapter = MetaAdapter(config.metadata, language=language)
            if meta_adapter.connect():
                # Set handbook type for per-handbook metadata support
                meta_adapter.set_handbook_type(template_type)
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
    output_dir = Path('test-output')  # Use consolidated test-output directory
    output_generator = OutputGenerator(output_dir, test_mode=args.test)
    
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
    html_dir = None
    
    # Generate markdown
    if output_format in ['markdown', 'both', 'all']:
        if args.separate_files:
            # Generate separate markdown files for each template
            templates_data = [
                (template.path.name, content)
                for template, content in zip(templates, processed_contents)
            ]
            
            md_result = output_generator.generate_separate_markdown_files(
                templates_data,
                language,
                template_type
            )
            all_warnings.extend(md_result.warnings)
            all_errors.extend(md_result.errors)
            
            if md_result.markdown_path:
                markdown_path = md_result.markdown_path
                # Extract count from warning message
                file_count = len(templates_data)
                logger.log_info(f"✓ Generated {file_count} separate markdown files in {markdown_path.parent}")
            
            # Generate TOC file
            templates_info = []
            for template in templates:
                # Extract template number and title from filename
                # Expected format: 0010_Template_Name.md
                filename = template.path.name
                filename_base = Path(filename).stem
                
                # Extract number (first 4 digits)
                template_number = filename_base[:4]
                
                # Extract title (everything after first underscore, replace underscores with spaces)
                title_part = filename_base[5:] if len(filename_base) > 5 else filename_base
                template_title = title_part.replace('_', ' ')
                
                templates_info.append((template_number, template_title, filename))
            
            toc_result = output_generator.generate_markdown_toc(
                templates_info,
                language,
                template_type
            )
            all_warnings.extend(toc_result.warnings)
            all_errors.extend(toc_result.errors)
            
            if toc_result.markdown_path:
                logger.log_info(f"✓ TOC file generated: {toc_result.markdown_path}")
        else:
            # Generate combined markdown file (existing behavior)
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
    if output_format in ['pdf', 'both', 'all']:
        if args.pdf_toc:
            # Generate PDF with table of contents
            templates_data = []
            for template, content in zip(templates, processed_contents):
                # Extract template number and title from filename
                # Expected format: 0010_Template_Name.md
                filename = template.path.name
                filename_base = Path(filename).stem
                
                # Extract number (first 4 digits)
                template_number = filename_base[:4]
                
                # Extract title (everything after first underscore, replace underscores with spaces)
                title_part = filename_base[5:] if len(filename_base) > 5 else filename_base
                template_title = title_part.replace('_', ' ')
                
                templates_data.append((template_number, template_title, content))
            
            pdf_result = output_generator.generate_pdf_with_toc(
                templates_data,
                language,
                template_type
            )
            all_warnings.extend(pdf_result.warnings)
            all_errors.extend(pdf_result.errors)
            
            if pdf_result.pdf_path:
                pdf_path = pdf_result.pdf_path
                logger.log_info(f"✓ PDF with TOC generated: {pdf_path}")
        else:
            # Generate PDF without TOC (existing behavior)
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
    
    # Generate HTML
    if output_format in ['html', 'all']:
        html_generator = HTMLOutputGenerator(output_dir, test_mode=args.test)
        
        # Extract filenames from templates
        filenames = [template.path.name for template in templates]
        
        html_result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            language,
            template_type
        )
        all_warnings.extend(html_result.get('warnings', []))
        all_errors.extend(html_result.get('errors', []))
        
        if html_result.get('html_dir'):
            html_dir = html_result['html_dir']
            file_count = len(html_result.get('files', []))
            logger.log_info(f"✓ HTML site generated: {html_dir} ({file_count} files)")
    
    # Calculate statistics
    processing_time = logger.get_elapsed_time()
    assembled_content = output_generator.assemble_markdown(processed_contents)
    
    output_size = 0
    if markdown_path and markdown_path.exists():
        output_size += markdown_path.stat().st_size
    if pdf_path and pdf_path.exists():
        output_size += pdf_path.stat().st_size
    if html_dir and html_dir.exists():
        # Sum up all HTML files
        for html_file in html_dir.glob('*.html'):
            output_size += html_file.stat().st_size
        # Include CSS file
        css_file = html_dir / 'styles.css'
        if css_file.exists():
            output_size += css_file.stat().st_size
    
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
