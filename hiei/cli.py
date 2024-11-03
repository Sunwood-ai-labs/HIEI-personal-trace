"""Command Line Interface for HIEI."""

import click
from rich.console import Console

console = Console()

@click.group()
def main():
    """HIEI - Personal Work Activity Tracker."""
    pass

@main.command()
def start():
    """Start monitoring activities."""
    console.print("[bold green]Starting HIEI monitoring...[/]")
    # TODO: Implement monitoring logic

@main.command()
@click.option('--edit', is_flag=True, help='Edit configuration file')
def config(edit):
    """Manage HIEI configuration."""
    if edit:
        console.print("[bold yellow]Opening configuration file...[/]")
        # TODO: Implement config editing

if __name__ == '__main__':
    main()
