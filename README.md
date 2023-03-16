# Sprint DB Manager

A python script which helps me to manage all the problems and add a database entry without much hassle. I decided to create this because I really thought it would make life easier in managing over 150+ problems in the directory.

The whole script is solely written in `python` and would link my `MySQL` database for easier management.

As of now, it would only run on linux systems since the file paths are only of linux, but if you are willing to go through the code, then you can easily change the code. Changing PDF Viewers would be upon you and I don't know as of now how you can do it on Windows.

![A beautiful view!](/commands.png)

## Installation
I'm assuming you have git and latest version of Python installed. If not, then install it using 
```bash
sudo apt install git
sudo apt install python3
```
Commands might differ on distros, but I'm sure you can download it easily. Then finally a simple `git clone` command to install the scripts.
```bash
git clone https://github.com/SatisfiedMagma/Sprint_DB_Manager
```
If not git, then just directly download the whole directory from [GitHub](https://github.com/SatisfiedMagma/Sprint_DB_Manager/archive/refs/heads/main.zip). 

Finally, go into the directory in which installed and use `python __main__.py` to run it.

## Usage and Commands
You will get all the help you need to operate the script by issuing 
```bash
python __main__.py --help
```
The usage of every command is given there in ample of detail. For example, say you want the details of command ``add`` like which arguments it will take, then simply issue 
```bash
python __main__.py add --help
```
