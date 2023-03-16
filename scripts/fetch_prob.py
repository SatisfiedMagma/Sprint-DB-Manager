import pyperclip
from code_converter import *
from rich.console import Console
from rich.syntax import Syntax
from rich.prompt import Confirm

def get_prob(prob_source):
    console = Console()

    prob_code = code_conv(prob_source)
    prob_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.tex"

    file = open(prob_path, 'rt')
    problem = file.read()
    file.close()

    begin = problem.find("\\begin{prob*}")
    end = problem.find("\\end{prob*}") + 11 #adding 11 because otherwise we just get index of \ of \end{prob}

    final_prob = problem[begin:end]
    final_prob_syntax = Syntax(final_prob, "latex")
    console.print(final_prob_syntax)
    
    clipboard_confirmation = Confirm.ask("[green]Do you want to copy the problem statement to your clipboard?[/green]", default = True)
    if clipboard_confirmation:
        pyperclip.copy(final_prob)
        console.print("\nCopied the problem statement to clipboard!", style = "bold green")
    else:
        console.print("\nNothing was copied.")