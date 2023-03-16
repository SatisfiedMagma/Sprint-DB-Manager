import pyperclip 
from code_converter import code_conv
from rich.console import Console
from rich.syntax import Syntax
from scripts.sql_commands import find_subj

def get_diag(prob_source):
    console = Console()
    
    prob_code = code_conv(prob_source)
    prob_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.tex"

    with open(prob_path, "rt") as file:
        diag = file.read()
    
    begin = diag.find("    \\begin{center}\n        \\begin{asy}")
    end = diag.find("        \\end{asy}\n    \\end{center}") + 34 # adding 34 because otherwise we just get index of \ of \end{center}
    
    if begin == -1:
        console.print(f"\nNo diagram found in the problem. The problem is from {find_subj(prob_code)}. Check once more!", style = "bold")
        exit()
    
    final_diag = diag[begin:end]
    final_diag_syntax = Syntax(final_diag, "latex")
    console.print(final_diag_syntax)
    pyperclip.copy(final_diag)
    console.print("\nCopied the diagram code(asy) to clipboard!", style = "bold green")