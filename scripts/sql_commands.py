import mysql.connector as sqlcon
import time
from rich.console import Console
from rich.prompt import Prompt
from code_converter import code_conv
from scripts.tables import table_creator
import os

password = os.environ.get("PASSWORD") #saved db password as environment variable

# Connecting SQL
Oly_Base = sqlcon.connect(host = 'localhost',
                          user = 'root',
                          passwd = password,
                          database = 'Oly_Base')

# We will now define a bunch of functions to make interacting easy with SQL database.

console = Console()

def probsql(prob_source):
    console = Console()
    prob_code = code_conv(prob_source)

    insert_str = "INSERT INTO Main (Contest, Category, Difficulty, Tags) Values(%s, %s, %s, %s)"

    category = Prompt.ask("1. Choose the problem subject", choices = ["A", "C", "G", "N", "Calc"])
    difficulty = Prompt.ask("2. Choose a problem difficulty", choices = ["E", "M", "H", "B"])
    tags = Prompt.ask("3. Enter all the problem tags you want to enter")

    insert_tup = (prob_code, category, difficulty, tags)

    cur_base = Oly_Base.cursor()
    cur_base.execute(insert_str, insert_tup)
    Oly_Base.commit()
    Oly_Base.close()
    console.log("Updating Database...", style = "bold light_green")
    time.sleep(0.3)
    console.log("Database entry added!", style = "bold green")


def rem_prob(prob_source):
    console = Console()
    prob_code = code_conv(prob_source)

    rem_str = "DELETE FROM Main WHERE Contest = %s"
    cur_base = Oly_Base.cursor()
    cur_base.execute(rem_str, (prob_code, ))
    Oly_Base.commit()
    Oly_Base.close()
    time.sleep(0.3)
    console.log("Database entry removed.", style = "bold")


def search(parameter, search_query):
    if parameter == "tags":
        tag_str = f"SELECT * FROM Main WHERE Tags LIKE '%{search_query}%'"
        cur_base = Oly_Base.cursor()
        cur_base.execute(tag_str)
        result = list(cur_base.fetchall())
        Oly_Base.close()
    
        console.log(f"Searching records in database with tags {search_query}...", style = "bold blue")
        time.sleep(0.5)
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
        time.sleep(0.5)
        table_creator(result)
    
        
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