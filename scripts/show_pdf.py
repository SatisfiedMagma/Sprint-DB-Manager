from code_converter import code_conv
import os
from rich.prompt import Prompt
import time
from rich.console import Console

def preview_pdf(prob_source):
    console = Console()
    prob_code = code_conv(prob_source)
    pdf_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.pdf"

    pdf_viewer = Prompt.ask("Choose PDF Viewer", choices = ["Z", "E", "e"], default = "zathura")
    if pdf_viewer == "Z" or pdf_viewer == "zathura":
        pdf_viewer = "zathura"
    else:
        pdf_viewer = "evince"

    console.log("Opening PDF...", style = "bold green")
    time.sleep(0.4)
    os.system(f"{pdf_viewer} {pdf_path}&")
