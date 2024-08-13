import os
import locale

locale.setlocale(locale.LC_ALL, '') 
os.system('cls')

#Putting down the components of each relevant augment
halphinale = {
    'Aegis Soul IV':    30,
    'Ael Domina':       10,
    'Ret Domina':       10,
    'Kvar Domina':      10,
    'Stira Domina':     10,
}

luxhalpinalebasic = {
    'Foundia':          10,
    'Aegis Soul IV':    150,
    'Ael Domina':       50,
    'Ret Domina':       50,
    'Kvar Domina':      50,
    'Stira Domina':     50,
}

luxhalpinalefull = {
    'Foundia':          10,
    'Halphinale':       5
}

gigasmaste = {
    'Gigas Might IV':       10,
    'Gigas Precision IV':   10,
    'Gigas Technique IV':    10,
}

glangigasmastebasic = {
    'Foundia':              10,
    'Gigas Might IV':       50,
    'Gigas Precision IV':   50,
    'Gigas Technique IV':    50,
}

glangigasmastefull = {
    'Foundia':      10,
    'Gigas Maste':  10
}

gladiasoul = {
    'Starl Soul':       10,
    'Eradi Soul IV':    30
}

grangladiasoulbasic = {
    'Starl Soul':       50,
    'Eradi Soul IV':    150,
    'Foundia':          10
}

grangladiasoulfull = {
    'Gladia Soul':  5,
    'Foundia':      10
}

granddreadkeeperi = {
    'Dread Keeper V':   10
}

granddreadkeeperiibasic= {
    'Dread Keeper V':   50,
    'Foundia':          10,
    'Dualble V':         30
}

granddreadkeeperiifull= {
    'Grand Dread Keeper I':   5,
    'Foundia':          10,
    'Dualble V':         30
}

highvkardomina ={
    'Kvar Sovern':  30,
    'Belgan Note':  150,
    'Lostral Note': 150
}

def calc(name, augment):
    print(f"\nComponents for {name}")
    for compName, compNo in augment.items():
        print(f"""    {compName} {compNo}x""")
    #temp key = price and value = total
    temp = []
    print("\nPlease enter the value of the following augments (ex: 10000)\nEnter 0 if you don't plan on buying") 
    for compName, compNo in augment.items():
        priceInput = input(f"{compName}: ")
        if not priceInput:
            priceInput = 0
        price = int(priceInput)
        total = int(price) * int(compNo)
        temp.append([price, total])
    index = 0
    grandTotal = 0
    print("\nCost Breakdown:")
    for compName, compNo in augment.items():        
        print(f"    {compName}: {compNo} * {temp[index][0]} = {temp[index][1]}") 
        grandTotal += temp[index][1]
        index += 1
    
    print(f"""
Grand Total to buy components {name}: {locale.format_string("%d", grandTotal, grouping=True)}
Sell for above this price to make profit (including tax): {locale.format_string("%d", (grandTotal * 1.30), grouping=True)}""")

print("Welcome to PSO2 Augment Price Calculator (APC)")

print("""
How to use:
APC multiplies the values of the current prices of the components of the selected augment (that the user inputs) by how many it requires to create the end product. At the end, it returns the total price as well as the necessary price (with tax) one needs to sell the end product to make a profit""")

programLoop = True
while programLoop:
    augmentSelect = input("""\nPlease select an augment (example: 1 for Halphinale)
    1       |   Halphinale
    2       |   Lux Halphinale (Basic Components)
    3       |   Lux Halphinale (5x Halphinale)
    4       |   Gigas Maste
    5       |   Glan Gigas Maste (Basic Components)
    6       |   Glan Gigas Maste (5x Gigas Maste)
    7       |   Gladia Soul
    8       |   Gran Gladia Soul (Basic Components)
    9       |   Gran Gladia Soul (5x Gladia Soul)
    10      |   Grand Dread Keeper I 
    11      |   Grand Dread Keeper II (Basic Components)
    12      |   Grand Dread Keeper II (5x GDKI)
    13      |   Highkvar Domina
input: """)

    match augmentSelect:
        case "1":
            calc("Halphinale", halphinale)
        case "2":
            calc("Lux Halphinale", luxhalpinalebasic)
        case "3":
            calc("Lux Halphinale", luxhalpinalefull)
        case "4":
            calc("Gigas Maste", gigasmaste)
        case "5":
            calc("Glan Gigas Maste", glangigasmastebasic)
        case "6":
            calc("Glan Gigas Maste", glangigasmastefull)
        case "7":
            calc("Gladia Soul", gladiasoul)
        case "8":
            calc("Gran Gladia Soul", grangladiasoulbasic)
        case "9":
            calc("Gran Gladia Soul", grangladiasoulfull)
        case "10":
            calc("Grand Dread Keeper I", granddreadkeeperi)
        case "11":
            calc("Grand Dread Keeper II", granddreadkeeperiibasic)
        case "12":
            calc("Grand Dread Keeper II", granddreadkeeperiifull)
        case "13":
            calc("Highkvar Domina", highvkardomina)
        case _:
            print("Sorry, please enter the number (1-12) corresponding to an augment")
    aftercare = input("Would you like to go again? (Y/N)\ninput: ")
    match aftercare:
        case "Y":
            programLoop = True
            os.system('cls')
        case "y":
            programLoop = True
            os.system('cls')
        case "":
            programLoop = True
        case "N":
            programLoop = False
        case "n":
            programLoop = False
            os.system('cls')
        case _:
            print("Invalid input")
            programLoop = False


input("\n\nThank you for using APC\nPress any key to continue...")
