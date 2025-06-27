# cli/main.py


import typer
from rich.console import Console
from scanner.trivy import run_trivy_scan
from scanner.config_loader import load_config
from scanner.gitleaks import run_gitleaks_scan

app = typer.Typer()
console = Console()

@app.command()
def scan():
    """Run configured security scans"""
    config = load_config()

    scanners = config.get("scanners", [])
    for scanner in scanners:
        name = scanner.get("name")
        enabled = scanner.get("enabled", False)

        if name == "trivy" and enabled:
            target = scanner.get("target", "alpine:latest")
            options = scanner.get("options", {})
            console.print(f"[bold magenta] Starting scan: {name.upper()} on {target}[/bold magenta]")
            run_trivy_scan(target)
        elif name == "gitleaks" and enabled:
            repo = scanner.get("target", ".")
            console.print(f"[bold magenta] Starting scan: {name.upper()} on {repo}[/bold magenta]")
            run_gitleaks_scan(repo)

    console.print("[bold green] All enabled scans completed![/bold green]")

if __name__ == "__main__":
    app()

