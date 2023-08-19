from os import chdir, mkdir
import datetime as dt
from code_converter import code_conv, prob_title
from rich.console import Console
from shutil import rmtree

console = Console()

def writer(prob_source):
    prob_code = code_conv(prob_source)
    prob_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}"
    
    title = prob_title(prob_source)

    #Default LaTeX Template
    current_datetime = dt.datetime.now() #Current_Date
    date = current_datetime.strftime("%d %B, %Y")

    prob_template = "\\documentclass[11pt]{scrartcl}\n\\usepackage[left=1.1in,right=1.1in]{geometry}\n\\usepackage{sprint}\n%Get the Sprint package from here:\n%https://github.com/SatisfiedMagma/hot_dotfiles/blob/main/texmf/tex/latex/local/The-Sprint-Package/sprint.sty\n\n\\rhead{" + title + "}\n%\\lhead{Pragyan Pranay \\today}\n\n\\begin{document}\n\\title{" + title + " Solution}\n\\author{Pragyan Pranay}\n" + "\\date{" + date + "}\n" + "\\maketitle\n\n\\tableofcontents\n\n\\section{Problem}\n\\begin{prob*}{(" + title + ")}\n\n\\end{prob*}\n\n\\newpage\n\n\\section{Solution}\n\n\n\\newpage \n\n\\section{Motivation and Comments} \n\n\\end{document}"

    mkdir(prob_path)
    tex_ext = f"{prob_path}/{prob_code}.tex"
    try:
        with open(tex_ext, "a") as tex_file:
            tex_file.write(prob_template)
        console.log(".tex file added!", style = "bold green")
    except FileExistsError:
        console.log("File already available, only database entry added.", style="bold green")

def unwriter(prob_source):
    console = Console()
    prob_code = code_conv(prob_source)
    oly_prob_path = "/home/pragyan/Documents/Maths-Olympiads/Problems/"
    chdir(oly_prob_path)
    try:
        rmtree(f"{oly_prob_path}/{prob_code}")
        console.log("Problem directory removed.")
    except FileNotFoundError:
        console.log("No such Problem directory. Nothing was deleted.")