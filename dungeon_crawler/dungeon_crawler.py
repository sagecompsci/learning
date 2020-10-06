import sys


def line():
    print("--------------------------------------------------------------------------")


copper_sword = 0
steel_sword = 0
helmet = 0
chestplate = 0


gold = 0
clear = 0
kill = 0


name = 0
room_Armor = 0
room_Man = 0
room_M1 = 0
room_M2 = 0
room_M3 = 0
room_M4 = 0
room_Gold = 0
room_Gold2 = 0
room_Check = 0





def start():
    global clear, kill

    while (clear == 1):
        sys.exit(0)
    while (kill == 1):
        sys.exit(0)
    print("You have entered the dungeon.")




def lobby(): #start room
    print("You are in the main entrance of the dungeon.")
    rooms = ['w','n']
    print("There are two rooms. One to the north, and one to the west.")
    choice = None
    while not choice in rooms:
        choice = input("Which room do you want to enter?").strip().lower()[0]  

        if choice == "w":
            line()
            room_m1()
        elif choice == "n":
            line()
            room_man()
        else:
            line()
            print("PICK AN ACTUAL ROOM PLEASE!")




def shop(): #room with man
    global gold, chestplate, steel_sword

    option_s = ['1','2']
    choice_s = None
    print("'I see you found some gold. Take a look at what I have for sale.'")
    print(f"You have {gold} pieces of gold.")
    print("1. Steel Sword 40 gold pieces")
    print("2. Chestplate 20 gold peices")
    print("3. Leave shop")
    while not choice_s in option_s:
        choice_s = input("'What would you like to buy?'").strip().lower()[0] 

        if choice_s == "1":
            if steel_sword == 0:
                if gold >= 40:
                    line()
                    print("You bought a Steel Sword!")
                    line()
                    gold -= 40
                    steel_sword += 1
                    shop()
                else:
                    line()
                    print("You do not have enough gold to buy this.")
                    line()
                    shop()
            else:
                line()
                print("You have already bought this item.")
                line()
                shop()
        elif choice_s == '2':
            if chestplate == 0:
                if gold >= 20:
                    line()
                    print("You bough a Chestplate!")
                    line()
                    gold -= 20
                    chestplate += 1
                    shop()
                else:
                    line()
                    print("You do not have enough gold to buy this.")
                    line()
                    shop()
            else:
                line()
                print("You have already bought this item.")
                line()
                shop()
        elif choice_s == '3':
            line()
            print("You leave the shop.")
            line()
            lobby()
        else:
            line()
            print("CHOOSE EITHER ONE, TWO OR THREE.")




def room_gold2(): #room s after m3
    global gold, room_Gold2

    if room_Gold2 == 0:
        print("You enter the room and find a chest with 30 peices of gold in it.")
        gold += 30
        print(f"Now you have {gold} pieces of gold.")
        print("You put the gold in a pouch, and leave the room.")
        line()
        room_Gold2 += 1
        room_m3()
    else:
        print("You have already taken the gold from the chest.")
        print("You leave the room.")
        line()
        room_m3()




def room_m4():  #last room after m3
    global steel_sword, chestplate, kill, clear

    option_m4 = ['y','n']
    choice_m4 = None
    while not choice_m4 in option_m4:
        choice_m4 = input("The monster is really strong, are you sure you want to enter?")

        if choice_m4 == 'y':
            line()
            if steel_sword == 1 and chestplate == 1:
                print("You enter the room, and the door closes behind you. It is dark.")
                print("You block the monsters first attack, but he attacks again.")
                print("You kill him.")
                line()
                print("YOU CLEARED THE DUNGEON!!!")
                clear += 1
                line()
                start()
                
            else:
                kill += 1
                print("You enter the room, and the door closes behind you. It is dark.")
                print("You block the monsters first attack, but he attacks again.")
                print("He kills you.")
                line()
                start()
        elif choice_m4 == 'n':
            line()
            room_m3()




def room_m3():  #room after check
    global steel_sword, chestplate, room_M3

    if room_M3 == 0:
        print("You enter the room, and a monster jumps out at you.")
        if steel_sword == 0 and chestplate == 0:
            print("The monster kills you.")
            line()
            kill += 1
            start()
        else:
            print("You kill the monster.")
            line()
            room_M3 +=1

    else:
        print("You have already killed the monster in this room.")
    option_M3 = ['w','s','e']
    choice_M3 = None
    print("There is a room to the west, on to the south, and one to the east.")
    while not choice_M3 in option_M3:
        choice_M3 = input("Where would you like to go?").strip().lower()[0] 

        if choice_M3 == 'w':
            line()
            room_check()
        elif choice_M3 == 's':
            line()
            room_gold2()
        elif choice_M3 == 'e':
            line()
            room_m4()
        else:
            line()
            print("CHOOSE A DIRECTION.")




def room_armor(): #room w after m1
    global helmet, room_Armor

    if room_Armor == 0:
        print("You enter the room and find a chest with a helmet in it")
        print("You put it on and leave the room.")
        helmet += 1
        room_Armor += 1
        line()
        room_m1()
    else:
        print("You enter the room. You have already taken the helmet.")
        option_a = ['y','n']
        choice_a = None

        while not choice_a in option_a:
            choice_a = input("Would you like to leave the room?").strip().lower()[0] 
            
            if choice_a == 'y':
                line()
                room_m1()
            elif choice_a == 'n':
                line()
                print("You stand in the room. An hour later, Chris comes in.")
                print("'What are you doing? Let's go.'")
                line()
                lobby()
            else:
                line()
                print("CHOOSE YES OR NO.")




def room_check():  #e2 after hall
    global room_Check, long_sword, chestplate, kill, helmet

    if room_Check == 0:
        if helmet == 0:
            print("You try to enter the room, but Chris stops you.")
            print("'If you try to pass this point as you are, you will die.'")
            print("'Come back when you have better stuff.'")
            line()
            room_hall()

        elif steel_sword == 0 and chestplate == 0:
            print("You try to enter the room, but Chris stops you.")
            print("'If you try to pass this point as you are, you will die.'")
            print("Come back when you have better stuff.")
            line()
            room_hall()
        else:
            room_Check +=1
            room_check()
    else:
        option_c = ['w','e']
        choice_c = None
        print("You enter the room. It is empty.")
        print("There is one room to the west, and one to the east.")
        while not choice_c in option_c:
            choice_c = input("Where would you like to go?").strip().lower()[0] 

            if choice_c == 'w':
                line()
                room_hall()
            elif choice_c == 'e':
                line()
                room_m3()
            else:
                line()
                print("CHOOSE AN ACTUAL ROOM PLEASE.")




def room_gold(): #room e1 in hall
    global gold, room_Gold

    if room_Gold == 0:
        print("You enter the room and find a chest in the middle of the room.")
        print("You open the chest, and find it full of gold. You recieve 30 gold peices.")
        gold += 30
        print("You put the gold in a pouch and leave the room.")
        room_Gold += 1
        line()
        room_hall()
    else:
        print("You enter the room, the chest is empty. You leave the room.")
        line()
        room_hall()




def room_m2(): #room w in hall
    global helmet, chestplate, steel_sword, room_M2, kill

    if room_M2 == 0:
        print("You enter the room, and you are attacked by a monster.")
        print("It looks stronger than the one you already deafeated.")
        option_m2 = ['1','2']
        choice_m2 = None
        print("You have two choices:")
        print("1. Run")
        print("2. Fight")
        while not choice_m2 in option_m2:
            choice_m2 = input("What would you like to do?").strip().lower()[0] 

            if choice_m2 == '1':
                line()
                room_hall()
            elif choice_m2 == '2':
                line()
                print("You attack the monster, and he fights back.")
                if helmet == 0 and chestplate == 0 and steel_sword == 0:
                    print("The monster kills you.")
                    kill += 1
                    line()
                    start()
                else:
                    print("The monster attacks, but you kill him.")
                    line()
                    room_M2 += 1
            else:
                line()
                print("CHOOSE EITHER ONE OR TWO.")
    else:
        print("You enter the room. You have already killed the monster.")
    option_M2 = ['y','n']
    choice_M2 = None
    while not choice_M2 in option_M2:
        choice_M2 = input("Would you like to leave the room?").strip().lower()[0] 

        if choice_M2 == 'y':
            line()
            room_hall()
        elif choice_M2 == 'n':
            line()
            print("You stand in the room, but you here a creepy noise coming from the corner. You leave the room.")
            line()
            room_hall()
        else:
            line()
            print("CHOOSE YES OR NO.")




def room_hall(): #room n after m1
    print("You enter a long hall. There are two doorways to the east,")
    print("one to the west, and one to the south.")
    option_h = ['e','w']
    choice_h = None
    while not choice_h in option_h:
        choice_h = input("Which direction do you want to go.").strip().lower()[0]   

        if choice_h == 'w':
            line()
            room_m2()
        if choice_h == 's':
            line()
            room_m1()
        elif choice_h == 'e':
            line()
            option_H = ['1','2']
            choice_H = None
            while not choice_H in option_H:
                choice_H = input("Do you want to go through door one, or two?").strip().lower()[0]  

                if choice_H == '1':
                    line()
                    room_gold()
                elif choice_H == '2':
                    line()
                    room_check()
                else:
                    line()
                    print("CHOOSE DOOR ONE OR DOOR TWO.")
        else:
            line()
            print("CHOOSE EAST OR WEST.")




def room_man(): #room  n in lobby
    global copper_sword, chestplate, steel_sword, room_Man, name, kill

    if room_Man == 0:
        print("You enter the room and see a man.")
        print("What would you like to say?")
        print("1. Can you help me?")
        print("2. Stay out of my dungeon.")
    

        says = ['1','2']
        speach = None
        while  not speach in says:
            speach = input("Choose a number.").strip().lower()[0]  

            if speach == "1":
                line()
                print("The man says 'I suppose I could help. I'm Chris.'")
                name = input("'What's your name?'")
                line()
                print("He gives you a sword and a map.")
                copper_sword = 0
                copper_sword += 1
                print(f"'Good luck out there {name}! Come back when you find some gold.'")
                room_Man +=1
                line()
                lobby()
            elif speach == "2":
                line()
                print("The man says 'No one owns this dungeon.'")
                print("He kills you.")
                kill += 1
                line()
                start()
            else:
                line()
                print("CHOOSE AN OPTION PLEASE!")

    
    elif gold > 0:
        line()
        shop()
        

        
    else:
        print("You enter the room. Chris is there.")
        print("'What are you doing here? Don't you have some monsters to kill?'")
        line()
        lobby()




def room_m1():  #room w in lobby
    global copper_sword, room_M1, kill

    if room_M1 == 0:
        print("You peak inside the room and see monsters.")
        options_m1 = ['1','2']
        print("1. Run")
        print("2. Fight")

        choice_m1 = None
        while not choice_m1 in options_m1:
            choice_m1 = input("What would you like to do?").strip().lower()[0]  
            
            if choice_m1 == "1":
                line()
                lobby()
            elif choice_m1 == "2":
                if copper_sword == 0: 
                    line()
                    print("The monster kills you.")
                    kill += 1
                    line()
                    start()
                else:
                    line()
                    print("You attack the monster and kill him!")
                    room_M1 += 1
                    line()
            else:
                line()
                print("CHOOSE ONE OR TWO.")
    else:
        print("You enter the room. You have already killed the monster.")
    print("There are three rooms, one to the north, west, and east.")
    option_M1 = ['n','e','w']
    choice_M1 = None
    while not choice_M1 in option_M1 :
        choice_M1 = input("Which door do you want to go through?").strip().lower()[0]   

        if choice_M1 == 'w':
            line()
            room_armor()
        elif choice_M1 == 'n':
            line()
            room_hall()
        elif choice_M1 == 'e':
            line()
            lobby()
        else:
            line()
            print("CHOOSE AN ACTUAL ROOM PLEASE.")




def start():    
    global clear, kill 

    while (clear == 1):
        sys.exit(0) 
    while (kill == 1):
        sys.exit(0) 
    print("You have entered the dungeon.")
        
    def lobby():
        print("You are in the main entrance of the dungeon.")
        rooms = ['w','n']
        print("There are two rooms. One to the north, and one to the west.")
        choice = None
        while not choice in rooms:
            choice = input("Which room do you want to enter?").strip().lower()[0]  

            if choice == "w":
                line()
                room_m1()
            elif choice == "n":
                line()
                room_man()
            else:
                line()
                print("PICK AN ACTUAL ROOM PLEASE!")
    lobby()




start()



