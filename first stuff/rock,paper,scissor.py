import random
choices = "r", "p", "s"
cp_choices =random.choice(choices)
users_choices = input("ROCK, PAPER or SCISSOR? (r\p\s):  ").lower
if users_choices is not choices: 
    input("invalid option")
if cp_choices=="r" and users_choices=="r":
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




    