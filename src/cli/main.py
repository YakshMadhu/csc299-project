"""Main CLI entry point for drawing tasks."""
import argparse
import sys
from src.cli.commands.add import add_task
from src.cli.commands.list import list_tasks


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Manage your drawing tasks from the command line"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new drawing task")
    add_parser.add_argument("description", type=str, help="Task description")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all drawing tasks")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        if args.command == "add":
            return add_task(args.description)
        elif args.command == "list":
            return list_tasks()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
