'''
Snake water gun game
1) 1 for snake(s)
2) -1 for water(w)
3) 0 for gun(g)
'''
import random
import os 
highest_score = 0
if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as f:
        lines = f.readlines()
        scores = []
        for line in lines:
            try:
                score_val = float(line.split(":")[-1].strip())
                scores.append(score_val)
            except:
                continue 
        
        if scores:
            highest_score = max(scores)

print(f"Welcome! The All-Time High Score is:: {highest_score}")

youDict={"S":1, "W":-1, "G":0}
reverseDict={1:"Snake", -1:"Water", 0:"Gun"}
n=0

while True:
    y = input("\nEnter S/Snake, W/Water, G/Gun (E to exit): ")
    y=y.upper()
    if y=="E":
        print(f"Final Score: {n}")
        with open("highscore.txt", "a") as f:
            f.write(f"Session Score: {n}\n")
        
        print("Score saved to highscore. Thanks for playing! Goodbye.")
        break
    if y not in youDict:
        print(f"Error! '{y}' is invalid. Use ONLY 'S', 'W', or 'G'.")
        continue

    comp= random.choice([-1,0,1])
    yn=youDict[y]
    print(f"Your choice is: {reverseDict[yn]} \nComputer choice is: {reverseDict[comp]}")
    if (comp == yn):
        print("It's a Draw!")
    else:
        if (comp == 1 and yn == 0): # Snake vs Gun
            print("You Win! Gun kills Snake.")
            n+=1
        elif (comp == 1 and yn == -1): # Snake vs Water
            print("You Lose! Snake drinks Water.")
            n-=1/2
        elif (comp == 0 and yn == 1): # Gun vs Snake
            print("You Lose! Gun kills Snake.")
            n-=1/2
        elif (comp == 0 and yn == -1): # Gun vs Water
            print("You Win! Gun drowns in Water.")
            n+=1
        elif (comp == -1 and yn == 1): # Water vs Snake
            print("You Win! Snake drinks Water.")
            n+=1
        elif (comp == -1 and yn == 0): # Water vs Gun
            print("You Lose! Gun drowns in Water.")
            n-=1/2
    print(f"!!Your Score is!!= {n}")
        



