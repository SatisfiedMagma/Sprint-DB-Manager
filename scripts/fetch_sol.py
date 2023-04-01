import pyperclip
from code_converter import code_conv
from rich.console import Console
from rich.syntax import Syntax
from rich.prompt import Confirm

def get_sol(prob_source):
    console = Console()
    prob_code = code_conv(prob_source)
    prob_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.tex"

    with open(prob_path, 'rt') as file:
        solution = file.read()

    begin = solution.find("\\begin{sol}")
    end = solution.find("\\end{sol}") + 9 # adding 9 because otherwise we just get index of \ of \end{sol}

    final_sol = solution[begin:end]
    final_sol_syntax = Syntax(final_sol, "latex")
    console.print(final_sol_syntax)
    
    clipboard_confirmation = Confirm.ask("[green]Do you want to copy the solution to your clipboard?[/green]", default = True)
    if clipboard_confirmation:
        pyperclip.copy(final_sol)
        console.print("\nCopied the solution to clipboard!", style = "bold green")
    else:
        console.print("\nNothing was copied.")