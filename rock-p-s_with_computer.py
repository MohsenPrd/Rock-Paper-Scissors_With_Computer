### Mohsen Pourdehghan

import random

print('{r: rock | p: paper | s: scissors}\n')
choiceList= ['r','p','s']

p1_1st= input("hi 'Player 1', Set your first choice: ")
while p1_1st != 'rock' and p1_1st != 'paper' and p1_1st != 'scissors':
    p1_1st= input("Again, Set your first choice: ")
    
p1_2nd= input("Set your second choice: ")
while p1_2nd != 'rock' and p1_2nd != 'paper' and p1_2nd != 'scissors':
    p1_2nd= input("Again, Set your second choice: ")
    
p1_3rd= input("Set your third choice: ")
while p1_3rd != 'rock' and p1_3rd != 'paper' and p1_3rd != 'scissors':
    p1_3rd= input("Again, Set your third choice: ")
p1_score= 0

co_1st= random.choice(choiceList)
co_2nd= random.choice(choiceList)
co_3rd= random.choice(choiceList)
co_score=0 

# First round compare

if p1_1st == co_1st :
    p1_score+= 0
    co_score+= 0

elif p1_1st == "r" and co_1st == "p":
    co_score+= 1

elif p1_1st == "p" and co_1st == "r":
    p1_score+= 1

elif p1_1st == "s" and co_1st == "r":
    co_score+= 1

elif p1_1st == "r" and co_1st == "scissors":
    p1_score+= 1

elif p1_1st == "p" and co_1st == "s":
    co_score+= 1

elif p1_1st == "s" and co_1st == "p":
    p1_score+= 1

# Second round compare

if p1_2nd == co_2nd :
    p1_score+= 0
    co_score+= 0

elif p1_2nd == "r" and co_2nd == "p":
    co_score+= 1

elif p1_2nd == "p" and co_2nd == "r":
    p1_score+= 1

elif p1_2nd == "s" and co_2nd == "r":
    co_score+= 1

elif p1_2nd == "r" and co_2nd == "s":
    p1_score+= 1

elif p1_2nd == "p" and co_2nd == "s":
    co_score+= 1

elif p1_2nd == "s" and co_2nd == "p":
    p1_score+= 1

# Third round compare

if p1_3rd == co_3rd :
    p1_score+= 0
    co_score+= 0

elif p1_3rd == "r" and co_3rd == "p":
    co_score+= 1

elif p1_3rd == "p" and co_3rd == "r":
    p1_score+= 1

elif p1_3rd == "s" and co_3rd == "r":
    co_score+= 1

elif p1_3rd == "r" and co_3rd == "s":
    p1_score+= 1

elif p1_3rd == "p" and co_3rd == "s":
    co_score+= 1

elif p1_3rd == "s" and co_3rd == "p":
    p1_score+= 1

print(f'\nscore of player 1: {p1_score}\nscore of computer: {co_score}')

# Final

if p1_score > co_score :
    print('Player 1 is the winner!')

elif p1_score == co_score :
    print('Draw!')
    
elif p1_score < co_score :
    print('computer is the winner!')

print(f"\ncomputers first choice: {co_1st}")
print(f"computers second choice: {co_2nd}")
print(f"computers third choice: {co_3rd}")
