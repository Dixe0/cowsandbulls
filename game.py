import random

number = []
atm_counter = 0

def makenum():
    for i in range(4):
        x = random.randrange(0, 9)
        number.append(x)

makenum()
def pgame():
    global atm_counter
    atm_counter += 1
    cows = 0
    bulls = 0
    uchoise = input("Please enter a 4 digits number: ")
    guss = []
    for i in range(4):
        guss.append(int(uchoise[i]))
    for i in range(4):
        for c in range(4):
            if(guss[i] == number[c]):
                cows += 1
    for x in range (4):
        if guss[x] == number[x]:
            bulls += 1
    print(f"Bulls:{bulls}")
    print(f"Cows: {cows}")
    print(f"Total ettempts: {atm_counter}")
    if bulls != 4:
        pgame()

pgame()
