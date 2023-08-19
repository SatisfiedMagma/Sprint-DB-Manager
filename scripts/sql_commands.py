import mysql.connector as sqlcon
from rich.console import Console
from rich.prompt import Prompt
from scripts.shortlist import IMO_adder, ISL_adder, ISL_remover
from code_converter import code_conv
from scripts.tables import table_creator
from os import environ

sql_password = environ.get("PASSWORD") #saved db password as environment variable

Oly_Base = sqlcon.connect(host = 'localhost',
                          user = 'root',
                          passwd = sql_password,
                          database = 'Oly_Base')

console = Console()

def prob_insertion(prob_code):
    insert_str = "INSERT INTO Main (Contest, Category, Difficulty, Tags) VALUES(%s, %s, %s, %s)"

    category = Prompt.ask("1. Choose the problem subject", choices = ["A", "C", "G", "N", "Calc"])
    difficulty = Prompt.ask("2. Choose a problem difficulty", choices = ["E", "M", "H", "B"])
    tags = Prompt.ask("3. Enter all the problem tags you want to enter")

    insert_tup = (prob_code, category, difficulty, tags)

    cur_base = Oly_Base.cursor()
    cur_base.execute(insert_str, insert_tup)
    Oly_Base.commit()
    Oly_Base.close()
    console.log("Entry added to Main DB!", style = "bold green")


def prob_deletion(prob_code):
    rem_str = f"DELETE FROM `Main` WHERE `Contest` = \"{prob_code}\""
    cur_base = Oly_Base.cursor()
    cur_base.execute(rem_str)
    Oly_Base.commit()
    Oly_Base.close()
    console.log("Database entry removed.", style = "bold")


#works nicely, for now
def probsql(prob_source):
    prob_code = code_conv(prob_source)

    if prob_code.startswith("IMO"):
        isl_position = Prompt.ask("Enter ISL position(0 if not known)")

        if isl_position == "0":
            prob_insertion(prob_code)
        else:
            IMO_adder(isl_position, prob_code)

    elif prob_code.startswith("ISL"):
        ISL_adder(prob_code)

    else:
        prob_insertion(prob_code)


def rem_prob(prob_source):
    prob_code = code_conv(prob_source)
    prob_deletion(prob_code)

    if prob_code.startswith("ISL"):
        ISL_remover(prob_code)


def search(parameter, search_query):
    if parameter == "tags":
        tag_str = f"SELECT * FROM Main WHERE Tags LIKE '%{search_query}%'"
        cur_base = Oly_Base.cursor()
        cur_base.execute(tag_str)
        result = list(cur_base.fetchall())
        Oly_Base.close()
    
        console.log(f"Searching records in database with tags {search_query}...", style = "bold blue")
        table_creator(result)
        console.print(f"A total of {len(result)} results have been found.")
    
    elif parameter == "contest":
        search_query = code_conv(search_query)
        contest_str = f"SELECT * FROM Main WHERE Contest LIKE '{search_query}%'"
        cur_base = Oly_Base.cursor()
        cur_base.execute(contest_str)
        result = cur_base.fetchall()
        Oly_Base.close()
    
        console.log(f"Searching for problem {search_query}...", style = "bold blue")
        table_creator(result)
        console.print(f"A total of {len(result)} results have been found.")

        
def show_db():
    db_str = f"SELECT * FROM Main"
    cur_base = Oly_Base.cursor()
    cur_base.execute(db_str)
    result = list(cur_base.fetchall())
    Oly_Base.close()
    
    table_creator(result)
    console.print(f"As of now, there are a total of {len(result)} problems in the database.")


def find_subj(prob_code: str):
    contest_str = f"SELECT Category FROM Main WHERE Contest=\"{prob_code}\""
    cur_base = Oly_Base.cursor()
    cur_base.execute(contest_str)
    result = cur_base.fetchone() #uniqueness, so fine
    Oly_Base.close()
    
    if result == None:
        return "Not found in Database"
    else:
        if result[0][0] == "A":
            return "Algebra"
        elif result[0][0] == "C":
            return "Combinatorics"
        elif result[0][0] == "G":
            return "Geometry"
        elif result[0][0] == "N":
            return "Number Theory"
        elif result[0][0] == "Calc":
            return "Calculus"
