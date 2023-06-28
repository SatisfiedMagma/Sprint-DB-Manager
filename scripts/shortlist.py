import mysql.connector as sqlcon
from os import environ
from code_converter import ISL_code
from rich.console import Console
from rich.prompt import Prompt

sql_password = environ.get("PASSWORD") # saved db password as environment variable

Oly_Base = sqlcon.connect(host='localhost',
                          user='root',
                          passwd=sql_password,
                          database='Oly_Base')

console = Console()

isl_cur = Oly_Base.cursor()

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
    insert_str_checklist = f"UPDATE ISL_Checklist SET Done=1 WHERE `Year`={isl_year} AND `Subject`='{position}'"

    insert_str = "INSERT INTO Main (Contest, Category, Difficulty, Tags) VALUES(%s, %s, %s, %s)"

    category = prob_code[-2]
    difficulty = Prompt.ask("1. Choose a problem difficulty", choices = ["E", "M", "H", "B"])
    tags = Prompt.ask("2. Enter all the problem tags you want to enter")

    insert_tup = (prob_code, category, difficulty, tags)

    isl_cur.execute(insert_str_checklist)
    isl_cur.execute(insert_str, insert_tup)
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