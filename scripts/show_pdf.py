from code_converter import code_conv
import os
import time
from rich.console import Console

def preview_pdf(prob_source):
    console = Console()
    prob_code = code_conv(prob_source)
    pdf_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.pdf"

    if os.path.isfile(pdf_path):
        console.log("Opening PDF...", style = "bold green")
        time.sleep(0.4)
        os.system(f"zathura {pdf_path}")
    else:
        console.print("Can't open PDF. File not found.")