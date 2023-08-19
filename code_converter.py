def code_conv(prob_source:str):
    prob_code = prob_source.replace(" ", "_")
    special_list = ["A", "C", "G", "N", "B", "T"] #Putnams are A and B + ISLs, T(team contests)
    prob_index = prob_code.find("/") + 1

    #shortlist detector
    if prob_code[prob_index] in special_list:
        prob_code = prob_code.replace("/", "_")
    else:
        prob_code = prob_code.replace("/", "_P")

    #if i do some error
    if prob_code.startswith("JMO"):
        prob_code = prob_code.replace("JMO", "USAJMO")

    prob_code = prob_code.upper()
    
    return prob_code

def ISL_id(prob_source:str):
    ISL = False
    if prob_source.startswith("ISL"):
        ISL = True

    return ISL

def prob_title(prob_source: str):
    title = prob_source

    if ISL_id(prob_source):
        title = title.replace("ISL", "IMO Shortlist")
        return title

    if "SL" in prob_source:
        title = title.replace("SL", "Shortlist")
        return title

    if "IND" in title:
        title = title.replace("IND", "India")
        return title

    if "B-Math" in prob_source or "B.Math" in prob_source:
        title = title.replace("B-Math", "B.Math")
        return title

    if "B-Stat" in prob_source or "B.Stat" in prob_source:
        title = title.replace("B-Stat", "B.Stat")
        return title

    return title

def ISL_code(IMO_code:str, ISL_position:str):
    if ISL_position == 0: return None
    
    ISL_CODE = code_conv(IMO_code)
    ISL_CODE = ISL_CODE.replace("IMO", "ISL")
    isl_prob = ISL_CODE[-2:]
    ISL_CODE = ISL_CODE.replace(isl_prob, ISL_position)
    
    return ISL_CODE