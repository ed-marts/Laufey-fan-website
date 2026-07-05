
print("\nWelcome to Beetlife!")
action = 0
age = 0
health = 100
happiness = 100
intelligence = 50
money = 0
agelimit = range(0, 81) 
import random
nameslist = ['Liam', 'Emma', 'Noah', 'Olivia', 'Elijah', 'Ava', 'Lucas', 'Mia']
snamelist = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller']
name = random.choice(nameslist)
sname =random.choice(snamelist)

print(f"Your name is {name} {sname}")
print(f"You are {age} old")


def show_stats():
    print(f"\nAge: {age}")
    print(f"Health: {health}")
    print(f"Happiness: {happiness}")
    print(f"Intelligence: {intelligence}")
    print(f"Money: ${money}")

while age <= 80 and health > 0:
     mf = (input("Move forward in time? (yes/no): ")).strip().lower()
     
     if mf == "yes":
        age += 1
        print(f"\nYou are now {age} years old.")
        show_stats()
        
        if age <= 1:
            print("\nWhat would you like to do?")
            print("1. Cry all night long")
            print("2. Spit on your parents")
            print("3. Be a quiet baby")
            action = int(input())

            
            if action == 1:
                happiness -= 10
                print("You cried all night long and your parents got annoyed.    - Happiness -10")
            elif action == 2:
                happiness -= 5
                print("You spit on your parents and they were not happy. - Happiness -5")
            elif action == 3:   
                happiness += 5
                print("You were a quiet baby and your parents were happy. + Happiness +5")
        if mf == "yes":
            age += 1
            print(f"\nYou are now {age} years old.")
            show_stats()
        
        if age <= 2 and age > 1:
            print("\nWhat would you like to do?")
            print("1. Cry all night long")
            print("2. Bite your parents")
            print("3. Be a quiet baby")
            action = int(input())

            
            if action == 1:
                happiness -= 10
                print("You cried all night long and your parents got annoyed.    - Happiness -10")
            elif action == 2:
                happiness -= 5
                print("You bit your parents and they were not happy. - Happiness -5")
            elif action == 3:   
                happiness += 5
                print("You were a quiet baby and your parents were happy. + Happiness +5")
            

        elif age < 5:
            print("\nWhat would you like to do?")
            print("1. Study (+Intelligence, -Happiness)")
            print("2. Work (+Money, -Health)")
            print("3. Party (+Happiness, -Health, Random Event?)")

        elif age < 18:
            print("\nWhat would you like to do?")
            print("1. Study (+Intelligence, -Happiness)")
            print("2. Work (+Money, -Health)")
            print("3. Party (+Happiness, -Health, Random Event?)")

else:
        print("You chose not to move forward in time.")
        exit()
  

# choice input should be inside the age blocks, not here
