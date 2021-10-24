
from random import randint
def main():
    print("roll dem dur dice")
    dice = input()
    roll(dice)
    
    if play_again():
        main()
    else:
        print("bye now")

def roll(*dice):
     print(sum(randint(1, die) for die in dice))

def play_again():
    print("Play again? y / n")
    answer = raw_input()
    if answer != "y" and  answer != "n":
        print("?")
    else:
        if answer == "y":
            return True 
        else:
            print("Better luck next time bitch!")
            return False

if __name__ == "__main__":
    main()




