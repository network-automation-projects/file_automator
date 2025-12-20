# Config File Automator (Python)

A command-line tool for safely backing up and modifying YAML/JSON configuration files with recursive placeholder replacement.

Built as hands-on practice for network automation and DevOps roles — specifically automating configuration management for infrastructure and network devices.

## Why This Project?
This tool demonstrates practical skills relevant to network reliability and automation engineering:
- Safe, timestamped backups before any changes
- Recursive modification of nested YAML and JSON structures (common in network device configs)
- Comprehensive logging and robust error handling
- CLI interface for easy integration into automation workflows
- Clean, modular code following Python best practices

Directly supports tasks like:
- Automating provisioning and configuration of network devices/services
- Streamlining workflows and reducing manual operations
- Managing configuration files across environments

## Features
- Scans a directory for `.yaml`, `.yml`, and `.json` files
- Creates timestamped backups in a `backups/` directory
- Recursively replaces placeholder values in nested structures
- Detailed logging of all actions and errors (`logs/automation.log`)
- Customizable via command-line arguments
- Graceful handling of parsing errors and unsupported files

## Requirements
- Python 3.6+
- `pyyaml` (for YAML support)

Install dependency:
```bash
pip install pyyaml

Project Structure
textfile_automator/
├── config_automator.py     # Main script
├── configs/                # Example config files (add your own)
├── backups/                # Generated backups
├── logs/                   # Automation logs
└── README.md
Usage
Basic (uses default placeholder → updated_value)
Bashpython config_automator.py configs
Custom placeholder replacement
Bashpython config_automator.py configs --placeholder old_server_ip --new_value 10.0.0.100
Help
Bashpython config_automator.py --help
Example Config Files
Add files like these to the configs/ directory:
configs/config1.yaml
YAMLserver:
  host: localhost
  port: 8080
  value: placeholder_value
configs/config2.json
JSON{
  "database": {
    "url": "mysql://localhost/db",
    "value": "placeholder_value"
  }
}
After running, originals are updated and backups are preserved.
Logging
All actions are logged to logs/automation.log with timestamps for auditability and debugging.
Future Extensions

Integration with version control (auto-commit changes)
Support for Jinja2 templating
Dry-run mode
Integration with configuration management tools (Ansible, etc.)

Built By
Rebecca Clarke
Working toward Senior Software Engineer / Network Automation roles
[GitHub Profile] | [LinkedIn] (add your links)

This project is part of a series of practical Python automation tools built to prepare for roles involving network reliability, observability, and infrastructure automation.
