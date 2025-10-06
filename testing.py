import random
while True:

    choices = ["r", "p", "s"]
    users_choices = input("ROCK, PAPER or SCISSOR? (r\p\s):  ").lower()
    cp_choices = random.choice(choices)
    if users_choices not in choices: 
        print("invalid option")
    elif cp_choices=="r" and users_choices=="r":
        print("you chose rock\ncomputer chose rock\nyou draw")
    elif cp_choices=="r" and users_choices=="p":
        print("you chose rock\ncomputer chose paper\nyou win")
    elif cp_choices=="p" and users_choices=="p":
        print("you chose paper\ncomputer chose paper\nyou draw")
    elif cp_choices=="p" and users_choices=="s":
        print("you chose paper\ncomputer chose scissor\nyou win")
    elif cp_choices=="s" and users_choices=="p":
        print("you chose scissor\ncomputer chose paper\nyou win")
    elif cp_choices=="s" and users_choices=="s":
        print("you chose scissor\ncomputer chose scissor\nyou draw")
    elif cp_choices=="s" and users_choices=="r":
        print("you chose scissor\ncomputer chose rock\nyou lose")
    elif cp_choices=="r" and users_choices=="s":
        print("you chose rock\ncomputer chose scissor\nyou lose")
    elif cp_choices=="p" and users_choices=="r":
        print("you chose paper\ncomputer chose rock\nyou lose")
    elif users_choices == "n":
        print("quit game")
        break

    