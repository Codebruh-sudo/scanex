To build a modular, YAML-driven CLI tool that integrates multiple security scanners (like Trivy, Gitleaks), parses their output, aggregates findings, and produces a unified report (in JSON and HTML), all with CI/CD support.





                            +---------------------------+
                          |     scanner_config.yaml    |
                          +---------------------------+
                                       |
                          +------------v------------+
                          |      CLI Entry Point     |
                          |       (main.py)          |
                          +------------+-------------+
                                       |
          +----------------------------+-----------------------------+
          |                            |                             |
+----------------+     +------------------------+     +----------------------+
| Trivy Plugin   |     |    Gitleaks Plugin     |     |  (Pluggable: Checkov, |
| trivy.py       |     |  gitleaks.py           |     |  Semgrep, etc.)       |
+----------------+     +------------------------+     +----------------------+
          |                            |                             |
          +------------+--------------+--------------+--------------+
                       |                             |
              +--------v---------+         +---------v----------+
              | JSON Output File |         | JSON Output File   |
              | trivy_output.json|         | gitleaks_output.json|
              +--------+---------+         +---------+----------+
                       |                             |
                       +-------------+---------------+
                                     |
                        +------------v------------+
                        |   report_builder.py     |
                        |  ➜ summary_report.json  |
                        +------------+------------+
                                     |
                        +------------v------------+
                        |  report_to_html.py      |
                        |  ➜ scan_report.html     |
                        +-------------------------+

⚙️ Module Breakdown
cli/main.py
Entry point for scans

Parses YAML config

Dispatches scanner plugins

CLI managed by Typer

scanner_config.yaml
Declares which tools are enabled

Defines input targets, flags, and report formats

Allows future plugins via config-driven behavior

scanner/trivy.py, scanner/gitleaks.py
Modular wrappers for each tool

Handles CLI invocation + output routing

report_builder.py
Parses raw JSONs

Aggregates key metrics (e.g., Trivy severities, secrets found)

Outputs unified JSON summary

report_to_html.py
Uses Jinja2 to render HTML report

Styled for readability

Summarizes results per scanner

🚀 DevOps / CI Integration
GitHub Actions workflow (.github/workflows/devsecops.yml)

Triggers on push/PR

Installs deps, runs scans, generates reports

Uploads scan_report.html as an artifact

🔌 Extensibility & Pluggability
New tools (e.g., Checkov, Semgrep) can be added by:

Adding a new plugin module (scanner/checkov.py)

Defining its config block in YAML

Hooking it into main.py dispatch map

No core logic needs to change.

  
  📁 Output Directory Structure
reports/
├── trivy_output.json
├── gitleaks_output.json
├── summary_report.json
└── scan_report.html

  
