import os
from code_converter import code_conv, ISL_id

def editor(prob_source):
    prob_code = code_conv(prob_source)

    prob_path = f"/home/pragyan/Documents/Maths-Olympiads/Problems/{prob_code}/{prob_code}.tex"
    os.system(f"vim {prob_path}")
