from rich.table import Table
from rich.console import Console

def table_creator(search_results:tuple):
    console = Console()
    search_results = list(search_results)
    table = Table(title = "Search Results", header_style = "bold purple")
    table.add_column("Contest", style = "green")
    table.add_column("Category", style = "blue")
    table.add_column("Difficulty", style = "cyan")
    table.add_column("Tags", justify = "center", style = "magenta")

    for entry in search_results:
        table.add_row(*entry)
        
    console.print(table)