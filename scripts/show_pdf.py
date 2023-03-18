from code_converter import code_conv
import os
from rich.prompt import Prompt
import time
from rich.console import Console
from scripts.sql_commands import find_subj

def preview_pdf(prob_source):
    console = Console()
    prob_code = code_conv(prob_source)
    pdf_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.pdf"

    subject = find_subj(prob_code)
    
    if subject == "Combinatorics" or subject == "Geometry":
        pdf_viewer = "evince"
    else:
        pdf_viewer = "zathura"

    console.log("Opening PDF...", style = "bold green")
    time.sleep(0.4)
    os.system(f"{pdf_viewer} {pdf_path}&")
