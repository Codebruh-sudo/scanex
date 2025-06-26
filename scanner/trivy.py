# scanner/trivy.py
import subprocess
from rich.console import Console

console = Console()

def run_trivy_scan(image: str):
    console.print(f"[bold cyan]🔍 Running Trivy scan on:[/bold cyan] {image}")
    try:
        result = subprocess.run(["trivy", "image", "--format", "json", image], capture_output=True, text=True)
        if result.returncode == 0:
            console.print("[green]✅ Scan completed successfully![/green]")
            with open("reports/trivy_output.json", "w") as f:
                f.write(result.stdout)
        else:
            console.print("[red]❌ Scan failed[/red]")
            console.print(result.stderr)
    except Exception as e:
        console.print(f"[red]⚠️ Error:[/red] {e}")

