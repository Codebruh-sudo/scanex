# scanner/gitleaks.py
import subprocess
from rich.console import Console

console = Console()

def run_gitleaks_scan(repo_path: str):
    console.print(f"[bold cyan]🔐 Running Gitleaks scan on:[/bold cyan] {repo_path}")
    try:
        result = subprocess.run(["gitleaks", "detect", "-s", repo_path, "--report-format", "json", "--report-path", "reports/gitleaks_output.json"],
                                capture_output=True, text=True)
        if result.returncode == 0:
            console.print("[green]✅ Secrets scan completed![/green]")
        else:
            console.print("[red]❌ Secrets found or scan failed[/red]")
            console.print(result.stderr)
    except Exception as e:
        console.print(f"[red]⚠️ Error:[/red] {e}")
