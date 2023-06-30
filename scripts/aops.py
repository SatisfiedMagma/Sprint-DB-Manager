from scripts.fetch_sol import aops_raw
from pyperclip import copy
from rich.console import Console
from rich.prompt import Prompt, Confirm
import re

console = Console()

def init_string(solution: str):
    gsolve_confirm = Confirm.ask("Was this a group solve?", default=False)
    init_str = ""
    if gsolve_confirm:
        members = Prompt.ask("Enter the person with whom you group-solved (separate names by comma)")
        member_list = members.split(",")
        
        path = "/home/pragyan/Documents/Maths-Olympiads/Collection/Group_Solve_Team.txt"
        with open(path, "r") as f:
            gsolve_team = f.readlines()
        
        
        for member in range(len(member_list)):
            for person in range(len(gsolve_team)):
                if member_list[member] in gsolve_team[person]:
                    gsolve_team[person] = gsolve_team[person].replace(f" {member_list[member]}\n", "")
                    member_list[member] = gsolve_team[person]
                    break
                
        init_str = "Solved with"
        
        if len(member_list) == 1:
            init_str += f" {member_list[0]}.\n\n"
        elif len(member_list) == 2:
            init_str += f" {member_list[0]} and {member_list[1]}.\n\n"
        else:
            init_str += f"{', '.join(member_list[:-1:])} and {member_list[-1]}.\n\n"
    
    comments_prob = Prompt.ask("Enter some entertaining comments?")
    if comments_prob != "":
        init_str = comments_prob + init_str
        solution = init_str + solution
    else:
        solution = init_str + solution
    
    return solution

def environ_replacer(solution: str):
    #claim
    pattern_claim = r"\\begin{claim}(.*?)\\end{claim}"
    replacement_claim = r"\n\n[b][color=red]Claim:[/b][/color]\1\n"
    solution = re.sub(pattern_claim, replacement_claim, solution, flags=re.DOTALL)
    
    #proof
    pattern_proof = r" \\begin{proof}(.*?)\\end{proof}"
    square_end = r"\1".strip() + r"$\\square$"
    replacement_proof = f"\n[i]Proof:[/i]{square_end}\n{'-'*35}\n"
    solution = re.sub(pattern_proof, replacement_proof, solution, flags=re.DOTALL)
    
    #lemma
    pattern_lemma = r"\\begin{lemma}\n(.*?)\\end{lemma}"
    replacement_lemma = r"\n[b][color=blue]Lemma:[/b][/color]\1"
    solution = re.sub(pattern_lemma, replacement_lemma, solution, flags=re.DOTALL)
    
    #asy
    pattern_asy = r"\\begin{center} \\begin{asy}(.*?)\\end{asy} \\end{center}"
    
    match = re.search(pattern_asy, solution, flags=re.DOTALL)
    if match:
        asy = match.group(1)
        split_final_asy = asy.split(";")
        split_final_asy.pop()
        final_asy = ""
        for line in range(len(split_final_asy)):
            split_final_asy[line] = split_final_asy[line].lstrip()
            final_asy += split_final_asy[line] + ";\n"
    
        replacement_asy = f"\n[asy]\n{final_asy}\n[/asy]"
        solution = re.sub(pattern_asy, replacement_asy, solution, flags=re.DOTALL)
    
    return solution

def replacer(solution: str):
    basic_replacements = [["\\NN", "\\mathbb{N}"],
                          ["\\RR", "\\mathbb{R}"],
                          ["\\QQ", "\\mathbb{Q}"],
                          ["\\CC", "\\mathbb{C}"],
                          ["\\dg", "^\\circ"],
                          ["\\dangle", "\\measuredangle"],
                          ["\\half", "\\frac{1}{2}"],
                          ["\\cycsum", "\\sum_{\\mathrm{cyc}}"],
                          ["\\item", "[*]"],
                          ["\\begin{itemize}", "\n[list]\n"],
                          ["\\end{itemize}", "[/list]\n"],
                          ["\\begin{enumerate}", "\n[list=1]\n"],
                          ["\\end{enumerate}", "[/list]\n"]
                          ]
    for element in basic_replacements:
        solution = solution.replace(element[0], element[1])
    
    #ceil
    pattern_ceil = r"\\ceil{(\w+)}"
    replacement_ceil = r"\\lceil \1 \\rceil"
    solution = re.sub(pattern_ceil, replacement_ceil, solution)
    
    #floor
    pattern_floor = r"\\floor{(.*?)}"
    replacement_floor = r"\\left\\lfloor \1 \\right\\rfloor"
    solution = re.sub(pattern_floor, replacement_floor, solution, flags=re.DOTALL)
    
    #overline
    pattern_ol = r"\\ol{(.*?)}"
    replacement_ol = r"\\overline{\1}"
    solution = re.sub(pattern_ol, replacement_ol, solution, flags=re.DOTALL)
    
    return solution

def AOPSer(prob_source):
    solution_list = aops_raw(prob_source)
    solution = ""

    for i in range(len(solution_list)):
        solution_list[i] = solution_list[i].lstrip()

    solution_list[0] = "[i]Solution:[/i] "
    solution_list[len(solution_list)-1] = "$\\blacksquare$"

    # fixing indentation
    for i in range(len(solution_list)):
        if solution_list[i].startswith("\\["):
            solution_list[i] = "\n" + solution_list[i]
        if solution_list[i].strip()[-2:] == "\\]":
            solution_list[i+1] = "\n" + solution_list[i+1]
        if solution_list[i].startswith("\\vspace"):
            solution += "\n"
        elif solution_list[i-1] == "\n":
            solution += solution_list[i].rstrip()
        else:
            solution += solution_list[i].rstrip() + " "
    
    solution = replacer(solution)
    solution = environ_replacer(solution)
    solution = init_string(solution)
    
    solution = solution.replace("\\newpage", "")
    
    copy(solution)