def code_conv(prob_source):
    prob_code = prob_source.replace(" ", "_")
    special_list = ["A", "C", "G", "N", "B"] #Putnams are A and B + ISLs
    prob_index = prob_code.find("/") + 1

    if prob_code[prob_index] in special_list:
        prob_code = prob_code.replace("/", "_")
    else:
        prob_code = prob_code.replace("/", "_P")

    return prob_code

def ISL_id(prob_source):
    ISL = False
    if prob_source.startswith("ISL") == True:
        ISL = True

    return ISL

def prob_title(prob_source):
    title = prob_source

    if ISL_id(prob_source):
        title = title.replace("ISL", "IMO Shortlist")
    elif "SL" in prob_source:
        title = title.replace("SL", "Shortlist")
    elif "IND" in title:
        title = title.replace("IND", "India")
    if "B-Math" in prob_source or "B.Math" in prob_source:
        title = title.replace("B-Math", "B.Math")
    if "B-Stat" in prob_source or "B.Stat" in prob_source:
        title = title.replace("B-Stat", "B.Stat")

    return title
