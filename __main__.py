#! /usr/bin/python3

import scripts
import typer
from rich.console import Console
from rich.prompt import Confirm

main_console = Console()
app = typer.Typer(name = "Sprint Database Manager", add_completion = False, help = "A python script which helps in management of Olympiad Problems in a MySQL Database.")

@app.command(short_help = "Converts LaTeX solution file for AoPS.")
def aops(prob_source: str):
    scripts.AOPSer(prob_source)


@app.command(short_help = "Adds a .tex file and SQL database entry.")
def add(prob_source: str):
    scripts.probsql(prob_source)
    scripts.writer(prob_source)


@app.command(short_help = "Only adds a .tex file.")
def tex(prob_source: str):
    scripts.writer(prob_source)


@app.command(short_help = "Only adds a database entry.")
def dbentry(prob_source: str):
    scripts.probsql(prob_source)


@app.command(short_help = "Removes .tex file and the database entry.")
def delete(prob_source: str):
    sure = Confirm.ask(f"[red]Data deleted through here [bold underline]may[/bold underline] only be recovered through git. Are you sure you want to delete [bold underline]{prob_source}?[/bold underline][/red]")
    if sure == False:
        main_console.print("No data was deleted.:smile:")
        exit()

    scripts.rem_prob(prob_source)
    scripts.unwriter(prob_source)


@app.command(short_help = "Searches all your files by the desired parameters.")
def search(parameter:str, search_query:str):
    scripts.search(parameter, search_query)


@app.command(short_help = "Gets the solution of requested problem.")
def sol(prob_source: str):
    scripts.get_sol(prob_source)


@app.command(short_help = "Gets the problem statement of the requested problem.")
def prob(prob_source: str):
    scripts.get_prob(prob_source)


@app.command(short_help = "Gets the diagram from the requested problem.")
def diag(prob_source: str):
    scripts.get_diag(prob_source)


@app.command(short_help = "Opens the PDF File of requested problem. Default program is Zathura.")
def pdf(prob_source: str):
    scripts.preview_pdf(prob_source)


@app.command(short_help = "Opens the problem file in Vim for editing.")
def edit(prob_source: str):
    scripts.editor(prob_source)


@app.command(short_help = "Displays the entire Database.")
def showdb():
    scripts.show_db()


if __name__ == "__main__":
    app()