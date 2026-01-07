# Config File Automator (Python)

Python CLI for automating structured file updates (YAML/JSON) with logging and safety checks.

Built as hands-on practice for network automation and DevOps roles - specifically automating configuration management for infrastructure and network devices.

## Why This Project?

I built this tool to practice making **safe, repeatable configuration changes** across lots of files — the kind of work that comes up constantly in network and infrastructure automation.

Rather than editing configs by hand, I wanted a simple CLI that could:
- back up files automatically,
- make structured changes reliably,
- and leave a clear audit trail when something went wrong.

This project helped me get comfortable with treating configuration changes as something that should be **scripted, logged, and reversible**, not ad hoc.


## Features

- Scans directories for YAML and JSON config files
- Creates timestamped backups before modifying anything
- Recursively updates nested values (common in real-world configs)
- Logs every action and error to a file for traceability
- Exposed as a CLI so it can be chained into other automation


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
