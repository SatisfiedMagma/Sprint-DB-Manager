import mysql.connector as sqlcon
import time
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from code_converter import code_conv
import os

password = os.environ.get("PASSWORD") #saved db password as environment variable

# Connecting SQL
Oly_Base = sqlcon.connect(host = 'localhost',
                          user = 'root',
                          passwd = password,
                          database = 'Oly_Base')

# We will now define a bunch of functions to make interacting easy with SQL database.


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
    console.log("Database entry added!", style="bold green")


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


def tag_search(tags: str):
    tag_str = f"SELECT * FROM Main WHERE Tags LIKE '%{tags}%'"
    cur_base = Oly_Base.cursor()
    cur_base.execute(tag_str)
    result = list(cur_base.fetchall())
    Oly_Base.close()
    
    #printing a nice table
    table = Table(title = "Search Results", header_style = "bold purple")
    console = Console()
    table.add_column("Contest", style = "green")
    table.add_column("Category", style = "blue")
    table.add_column("Difficulty", style = "cyan")
    table.add_column("Tags", justify = "center", style = "magenta")

    for entry in result:
        table.add_row(*entry)
    console.log(f"Searching records in database with tags {tags}...", style = "bold blue")
    time.sleep(0.5)
    console.print(table)
    console.print(f"A total of {len(result)} results have been found.")


def show_db():
    db_str = f"SELECT * FROM Main"
    cur_base = Oly_Base.cursor()
    cur_base.execute(db_str)
    result = list(cur_base.fetchall())
    Oly_Base.close()
    
    #printing a nice table
    table = Table(title = "Search Results", header_style = "bold purple")
    console = Console()
    table.add_column("Contest", style = "green")
    table.add_column("Category", justify = "center", style = "blue")
    table.add_column("Difficulty", justify = "center", style = "cyan")
    table.add_column("Tags", justify = "center", style = "magenta")

    for entry in result:
        table.add_row(*entry)
    console.print(table)
    console.print(f"As of now, there are a total of {len(result)} problems in the database.")

def find_subj(prob_code: str):
    contest_str = f"SELECT Category FROM Main WHERE Contest=\"{prob_code}\""
    cur_base = Oly_Base.cursor()
    cur_base.execute(contest_str)
    result = cur_base.fetchone() #uniqueness, so fine
    Oly_Base.close()
    
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