import os
from rich.console import Console
from rich.prompt import Prompt
import time

def handouts(resource = None):
    console = Console()

    book_path = "/home/pragyan/Documents/Maths-Olympiads/Handouts_Books"

    if resource:
        if resource == "mont" or resource == "MONT":
            console.print("Opening MONT...", style = "bold green")
            time.sleep(0.18)
            os.system(f"open {book_path}/MONT.pdf&")
        if resource == "egmo" or resource == "EGMO":
            console.print("Opening EGMO...", style = "bold green")
            time.sleep(0.18)
            os.system(f"open {book_path}/EGMO_Geo.pdf&")
        if resource == "pablo" or resource == "combo":
            console.print("Opening Pablo Combinatorics...", style = "bold green")
            time.sleep(0.18)
            os.system(f"open {book_path}/Pablo_Combo.pdf&")
    else:
        for i in range(len(os.listdir(book_path))):
            console.print(f"{i+1}.", os.listdir(book_path)[i])

        book_list_no = list(range(1,len(os.listdir(book_path))+1))
        for j in range(len(book_list_no)):
            book_list_no[j] = str(book_list_no[j])

        open_book = Prompt.ask("Choose the handout of your choice", choices = book_list_no)
        pdf_viewer = Prompt.ask("Choose PDF Viewer", choices = ["Z", "E", "e"], default = "zathura")
        if pdf_viewer == "Z" or pdf_viewer == "zathura":
            pdf_viewer = "zathura"
        else:
            pdf_viewer = "evince"
        console.log(f"[bold green]Opening {os.listdir(book_path)[int(open_book) - 1]}...[/bold green]")
        time.sleep(0.2)
        os.system(f"{pdf_viewer} {book_path}/{os.listdir(book_path)[int(open_book) - 1]}&")
