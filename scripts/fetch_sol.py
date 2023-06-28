from pyperclip import copy
from code_converter import code_conv
from rich.console import Console
from rich.syntax import Syntax
from rich.prompt import Confirm
import re

console = Console()

def get_sol(prob_source):
    prob_code = code_conv(prob_source)
    prob_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.tex"

    with open(prob_path, "r") as file:
        solution = file.read()
    
    pattern = r"\\begin{sol}\n(.*?)\\end{sol}"
    match = re.search(pattern, solution, flags=re.DOTALL)
    
    if match:
        final_sol = match.group(0)

    final_sol_syntax = Syntax(final_sol, "latex")
    
    console.print(final_sol_syntax)
    
    clipboard_confirmation = Confirm.ask("[green]Do you want to copy the solution to your clipboard?[/green]", default = True)
    
    if clipboard_confirmation:
        copy(final_sol)
        console.print("\nCopied the solution to clipboard!", style = "bold green")
    else:
        console.print("\nNothing was copied.")

def aops_raw(prob_source):
    prob_code = code_conv(prob_source)
    prob_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.tex"

    with open(prob_path, "r") as file:
        solution = file.readlines()
    
    start = 0
    for line in solution:
        start += 1
        if line.startswith("\\begin{sol}"):
            break
    end = 0
    for line in solution:
        end += 1
        if line.startswith("\\end{sol}"):
            break
    
    solution = solution[start-1:end:]
    
    return solution