import argparse
import os
import json

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from scanner.scan_directory import scan_directory
from reporters.json_reporter import json_reporter

console = Console()

def is_path_exists(path):
    return os.path.exists(path)

def main():
    parser = argparse.ArgumentParser(description="[bold cyan]Secret Seeker[/bold cyan] - Secret Scanner")
    parser.add_argument('path', help="Path to scan")
    parser.add_argument('--output', default="report.json", help="Output file")
    args = parser.parse_args()

    if not is_path_exists(args.path):
        console.print(f"[bold red]Error:[/bold red] Path '{args.path}' does not exist.")
        exit(1)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Scanning files for secrets...", total=None)
        findings = scan_directory(args.path)

    report = json_reporter(findings)

    with open(args.output, "w", encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    console.print(f"\n[bold green]Scan Complete![/bold green]")
    console.print(f"Found [bold yellow]{len(findings)}[/bold yellow] potential secrets.")
    console.print(f"Report saved to: [bold underline]{args.output}[/bold underline]")

if __name__ == '__main__':
    main()