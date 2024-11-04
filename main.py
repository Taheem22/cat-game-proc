cat_attributes = {
    "intelligence": 50,
    "energy": 50,
    "weight": 4,
    "happiness": 50,

}

print("Welcome to my cat game!")

name = input("Enter name: ")
colour=input("what is the colour of your cat: ")


while True:
    
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats!4.feed cat")

    if option == '1':
        cat_attributes["energy"]-=10
        cat_attributes["happiness"]+=10
        cat_attributes["weight"]-=0.2

        pass

    elif option == '2':
        cat_attributes["intelligence"]+=10
        cat_attributes["happiness"]+=5

        pass
    elif option=="3":
        print(cat_attributes)
    elif option==4:
        cat_attributes["energy"]+=10
        cat_attributes["weight"]+=0.5
        pass


    if cat_attributes['energy'] < 0:
        print("well done, youve killed your cat...")
        break

        
    elif cat_attributes["happiness"]<20:
        print("your cats a but depressed, play with it to cheer it up")
    
    elif cat_attributes["intelligence"]<25:
        print("teach your cat stuff, its a bit dumb ")
    
    elif cat_attributes["weight"]<1:
        print("well done you killed your cat sicko... ")

    elif cat_attributes["weight"]>8:
        print("your cat is overweight, it has died")