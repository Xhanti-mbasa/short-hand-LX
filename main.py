import subprocess
import sys

def ascii():
    print("""
    How to use:
    For the first option to replace the (git add .) use shorthand (The replacement script) and the original script (git add .)
    For one-liner scripts the script doesn't have to be a git script, for example: replacing (ls > l)
    """)
ascii()
# #options
# zsh = 1
# bash = 2

# TODO add more structure and features.
def alias():
    shell_options = str(input(f"Enter your shell type:\n1. zsh\n2. bash\n:")).lower()
    
    if  shell_options != "1" or "2":
        print("You didn't choose a valid option zsh will be set as the default.")
    elif shell_options == "1":
        shell_options = "./zshrc"
    elif shell_options == "2":
        shell_options = "./bashrc"

    short_hand = input("Type out your short hand: ")
    command = input("Now the command you'll be replacing: ")
    verification_input = input("Are you sure you want to execute this command? Y/n: ").lower().strip()

    if verification_input == "y":
        original_command = f"echo 'alias {short_hand}='{command}'' >> {shell_options}"
        subprocess.run(original_command, capture_output=True, text=True)
        print(original_command)
    else:
        sys.exit("Cancelled")


# TODO add execution safety.
def simple_command():
    simple_command1 = input("Type out a command: ")
    subprocess.run(simple_command1, capture_output=True, text=True)


# simple_command()
alias()

