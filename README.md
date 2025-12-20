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
