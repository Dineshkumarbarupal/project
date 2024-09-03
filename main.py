import random

def game():
    computer = random.choice ([2,-1,0])
    your_input = input("Enter your choise: ")
    yourdict = {"s": 2,"w": -1, "g": 0}
    new_dict = {2:"snack", -1: "water", 0 : "gun" }

    you = yourdict[your_input]

    print(f"computer choise = {new_dict[computer]} and you choise = {new_dict[you]} ")
          
    if computer == you:
        print("this is drrow , try next time:  ")

    else:
        if computer == 2 and you == -1:
            print("you loss")
        elif computer == 2 and you == 0:
            print("you win")
        elif computer == -1 and you == 2:
            print("you win")
        elif computer == -1 and you == 0:
            print("you loss")
        elif computer == 0 and you == 2:
            print("you loss")
        elif computer == 0 and you == -1:
            print("you win")
        else:
            print("something went wrong")

game()    
game()    
game()    
game()    
game()    
game()    
game()    
game()    
game()    
        
        
        
        
# mydict = {
#     "name": "dinesh",
#     "age": 19
#           }        

# print(mydict["name"])
        
    








