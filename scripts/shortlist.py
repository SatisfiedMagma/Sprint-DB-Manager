import mysql.connector as sqlcon
from os import environ
from code_converter import ISL_code
from rich.console import Console
from rich.prompt import Prompt, Confirm

sql_password = environ.get("PASSWORD") # saved db password as environment variable

Oly_Base = sqlcon.connect(host='localhost',
                          user='root',
                          passwd=sql_password,
                          database='Oly_Base')

console = Console()

isl_cur = Oly_Base.cursor()

def db_adder(year):
    A_cnt = Prompt.ask("Enter number of Algebra problems")
    C_cnt = Prompt.ask("Enter number of Combinatorics problems")
    G_cnt = Prompt.ask("Enter number of Geometry problems")
    N_cnt = Prompt.ask("Enter number of Number Theory problems")
    subjects = [["A", A_cnt], ["C", C_cnt], ["G", G_cnt], ["N", N_cnt]]
    
    def insert_isl_checklist(subject, isl_year):
        insert_str_checklist_query = f"INSERT INTO ISL_Checklist (Year, Subject, Done) VALUES({isl_year}, '{subject}', 0)"
        isl_cur.execute(insert_str_checklist_query)
    
    for subject in subjects:
        for position in range(1,int(subject[1])+1):
            insert_isl_checklist(f"{subject[0]}{position}", year)
    Oly_Base.commit()
            
    console.log(f"Year {year} added to Checklist ✅\n", style = "bold green")

#will be used if ISL position != 0, won't be used as of now
def IMO_adder(position, IMO_code: str):
    ISL_CODE = ISL_code(IMO_code, position)
    imo_year = ISL_CODE[4:8]
    insert_str_checklist = f"UPDATE ISL_Checklist SET Done=1 WHERE `Year`={imo_year} AND `Subject`='{position}'"

    insert_str = "INSERT INTO Main (Contest, Category, Difficulty, Tags) VALUES(%s, %s, %s, %s)"

    category = Prompt.ask("1. Choose the problem subject", choices = ["A", "C", "G", "N", "Calc"])
    difficulty = Prompt.ask("2. Choose a problem difficulty", choices = ["E", "M", "H", "B"])
    tags = Prompt.ask("3. Enter all the problem tags you want to enter")

    insert_tup = (IMO_code, category, difficulty, tags)

    isl_cur.execute(insert_str_checklist)
    isl_cur.execute(insert_str, insert_tup)
    Oly_Base.commit()

    console.log("Entry added to Main DB!", style = "bold green")
    console.log("Added to Checklist ✅", style = "bold green")

    Oly_Base.close()


#will be used to add ISLs in database
def ISL_adder(prob_code):
    isl_year = prob_code[4:8]
    position = prob_code[-2:]
    
    
    #check if year available or not in checklist
    isl_cur.execute(f"SELECT COUNT(*) FROM ISL_Checklist WHERE `Year` = {isl_year}")
    rec_cnt = isl_cur.fetchone()[0]
    
    while rec_cnt == 0:
        console.print(f"The year {isl_year} is not yet added to checklist.")
        db_add_confirm = Confirm.ask(f"Should we add {isl_year} now?")
        if db_add_confirm:
            db_adder(isl_year)
            isl_cur.execute(f"SELECT COUNT(*) FROM ISL_Checklist WHERE `Year` = {isl_year}")
            rec_cnt = isl_cur.fetchone()[0]
        else:
            console.print("ISL Problems can't be added if they're not in checklist.")
            exit()
    else:
        insert_str_checklist = f"UPDATE ISL_Checklist SET Done=1 WHERE `Year`={isl_year} AND `Subject`='{position}'"

        insert_main_str = "INSERT INTO Main (Contest, Category, Difficulty, Tags) VALUES(%s, %s, %s, %s)"

        category = prob_code[-2]
        difficulty = Prompt.ask("1. Choose a problem difficulty", choices = ["E", "M", "H", "B"])
        tags = Prompt.ask("2. Enter all the problem tags you want to enter")

        insert_tup = (prob_code, category, difficulty, tags)

        isl_cur.execute(insert_str_checklist)
        isl_cur.execute(insert_main_str, insert_tup)
        Oly_Base.commit()

        console.log("Added to Checklist ✅", style = "bold green")
        console.log("Entry added to Main DB!", style = "bold green")

        Oly_Base.close()

def ISL_remover(prob_code):
    isl_year = prob_code[4:8]
    position = prob_code[-2:]
    ISL_rem_str = f"UPDATE ISL_Checklist SET Done=0 WHERE Year = \"{isl_year}\" AND Subject=\"{position}\""
    
    isl_cur.execute(ISL_rem_str)
    Oly_Base.commit()
    Oly_Base.close()
    
    console.log("Removed from checklist ❌", style = "bold")