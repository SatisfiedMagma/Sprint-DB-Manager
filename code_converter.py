def code_conv(prob_source):
    prob_code = prob_source.replace(" ", "_")
    special_list = ["A", "C", "G", "N", "B", "T"] #Putnams are A and B + ISLs, T(team contests)
    prob_index = prob_code.find("/") + 1

    #shortlist detector, can't be made better since it detects ISL and other SLs as well
    if prob_code[prob_index] in special_list:
        prob_code = prob_code.replace("/", "_")
    else:
        prob_code = prob_code.replace("/", "_P")

    #if i do some error
    if prob_code.startswith("JMO") or prob_code.startswith("jmo"):
        prob_code = prob_code.replace("JMO", "USAJMO")

    return prob_code

def ISL_id(prob_source):
    ISL = False
    if prob_source.startswith("ISL"):
        ISL = True

    return ISL

def prob_title(prob_source):
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
