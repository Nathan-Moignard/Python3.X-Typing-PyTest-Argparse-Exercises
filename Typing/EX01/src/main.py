##
## EPITECH PROJECT, 2020
## Python3.X-Typing-PyTest-Argparse-Exercises
## File description:
## main
##

def core() -> type:
    return_value : int = 0

    print("Hello have you modified the output type of core ?")
    if (input("Are you ready for the next exercise ? [YES/NO]\n") == "YES"):
        print ("Now do mypy to check if the is no issue.")
        return_value = 1
    else:
        print("Now go in main.py and modify the output type to the right thing.")
        return_value = 84
    return (return_value)