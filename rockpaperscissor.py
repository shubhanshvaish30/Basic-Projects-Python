import random
print("**********Welcome to ROCK, PAPER AND SCISSOR GAME**********")
print("Rules of the game:\nRock vs Scissor =>> Rock\nPaper vs Rock =>> Paper\nScissor vs Paper=>> Scissor")
while(True):
    print("\n1.Rock\n2.Paper\n3.Scissor")
    user_ch=int(input("Enter your choice:"))
    comp_ch=random.randrange(1,3)
    if(user_ch==1):
        print("\nUser choice:Rock")
    elif(user_ch==2):
        print("\nUser choice:Paper")
    else:
        print("\nUser choice:Scissor")
    if(comp_ch==1):
        print("\nComputer choice:Rock")
    elif(comp_ch==2):
        print("\nComputer choice:Paper")
    else:
        print("\nComputer choice:Scissor")
    if(user_ch==comp_ch):
        print("\nIt's Draw!")
        x=input("\nDo you want to play again?\nY/N:")
        if x=='Y' or x=='y':
            continue
        else:
            break
    elif user_ch==1 and comp_ch==2:
        print("\nUser vs Computer:\nRock vs Paper=>> COMPUTER WINS!!!!")
        x=input("\nDo you want to play again?\nY/N:")
        if x=='Y' or x=='y':
            continue
        else:
            break
    elif user_ch==2 and comp_ch==1:
        print("\nUser vs Computer:\nPaper vs Rock=>> User WINS!!!!")
        x=input("\nDo you want to play again?\nY/N:")
        if x=='Y' or x=='y':
            continue
        else:
            break
    elif user_ch==2 and comp_ch==3:
        print("\nUser vs Computer:\nPaper vs Scissor=>> Computer WINS!!!!")
        x=input("\nDo you want to play again?\nY/N:")
        if x=='Y' or x=='y':
            continue
        else:
            break
    elif user_ch==3 and comp_ch==2:
        print("\nUser vs Computer:\nScissor vs Paper=>> User WINS!!!!")
        x=input("\nDo you want to play again?\nY/N:")
        if x=='Y' or x=='y':
            continue
        else:
            break
    elif user_ch==1 and comp_ch==3:
        print("\nUser vs Computer:\nRock vs Scissor=>> User WINS!!!!")
        x=input("\nDo you want to play again?\nY/N:")
        if x=='Y' or x=='y':
            continue
        else:
            break
    elif user_ch==3 and comp_ch==1:
        print("\nUser vs Computer:\n Scissor vs Rock=>> Computer WINS!!!!")
        x=input("\nDo you want to play again?\nY/N:")
        if x=='Y' or x=='y':
            continue
        else:
            break