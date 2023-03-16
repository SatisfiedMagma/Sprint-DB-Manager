import time
import os
from rich.console import Console

def change_previewer(previewer):
    home = "/home/pragyan"
    os.chdir(home)
    console = Console()
    
    evince = ["e", "E", "Evince", "evince"]
    zathura = ["z", "Z", "zathura", "Z"]
    
    x3 = "sub asy {return system(" + "\"asy " + "\\\"$_[0]\\\"\");}"+ "\n" + "add_cus_dep(\"asy\",\"eps\",0,\"asy\");" + "\n" + "add_cus_dep(\"asy\",\"pdf\",0,\"asy\");" + "\n" + "add_cus_dep(\"asy\",\"tex\",0,\"asy\");" + "\n\n" + "# vim: ft=perl"
    
    latexmkrc_file = open(".latexmkrc", "w")
    if previewer in evince:
        edit = "#$pdf_previewer = \"zathura %O %S &> /dev/null &\";" + "\n" + "$pdf_previewer = 'start evince 2> /dev/null'; #(to switch previewers)" + "\n" + x3
        latexmkrc_file.write(edit)
        latexmkrc_file.close()
        time.sleep(0.2)
        console.log("PDF Viewer Changed to Evince!", style = "bold green")
    elif previewer in zathura:
        edit = "$pdf_previewer = \"zathura %O %S &> /dev/null &\";" + "\n" + "#$pdf_previewer = 'start evince 2> /dev/null'; #(to switch previewers)" + "\n" + x3
        latexmkrc_file.write(edit)
        latexmkrc_file.close()
        time.sleep(0.2)
        console.log("PDF Viewer Changed to Zathura!", style = "bold green")