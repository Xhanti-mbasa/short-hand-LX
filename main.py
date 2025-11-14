import subprocess

# TODO add more structure and features.
def alias():
    shell_options = input("Enter your shell type:\n(1)./bashrc\n(2)./zshrc\n:")
    short_hand = input("Type out your short hand: ")
    command = input("Now the command you'll be replacing: ")
    original_command = f"echo 'alias {short_hand}='{command}'' >> {shell_options}"
    subprocess.run(original_command, shell=True)
# TODO add execution safety.
def simple_command():
    simple_command1 = input("Type out a command: ")
    subprocess.run(simple_command1, shell=True)


simple_command()
# alias()
