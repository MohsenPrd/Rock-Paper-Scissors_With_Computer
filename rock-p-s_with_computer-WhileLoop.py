### Mohsen Pourdehghan

import random

print('{rock | paper | scissors}\n')

choiceList_for_comp= ['rock','paper','scissors']
p1_list = []
comp_list =[]

p1_score= 0
co_score=0 

p1_1= input("hi 'Player 1', Set your first choice: ")
while p1_1 != 'rock' and p1_1 != 'paper' and p1_1 != 'scissors':
    p1_1= input("Again, Set your first choice: ")
p1_list.append(p1_1)
    
p1_2= input("Set your second choice: ")
while p1_2 != 'rock' and p1_2 != 'paper' and p1_2 != 'scissors':
    p1_2= input("Again, Set your second choice: ")
p1_list.append(p1_2)

p1_3= input("Set your third choice: ")
while p1_3 != 'rock' and p1_3 != 'paper' and p1_3 != 'scissors':
    p1_3= input("Again, Set your third choice: ")
p1_list.append(p1_3)


co_1= random.choice(choiceList_for_comp)
co_2= random.choice(choiceList_for_comp)
co_3= random.choice(choiceList_for_comp)

comp_list.append(co_1)
comp_list.append(co_2)
comp_list.append(co_3)

# First round to third round compare
x=0
while x <= 2 :
    if p1_list[x] == comp_list[x] :
        p1_score+= 0
        co_score+= 0

    elif p1_list[x] == "rock" and comp_list[x] == "paper":
        co_score+= 1

    elif p1_list[x] == "paper" and comp_list[x] == "rock":
        p1_score+= 1

    elif p1_list[x] == "scissors" and comp_list[x] == "rock":
        co_score+= 1

    elif p1_list[x] == "rock" and comp_list[x] == "scissors":
        p1_score+= 1

    elif p1_list[x] == "paper" and comp_list[x] == "scissors":
        co_score+= 1

    elif p1_list[x] == "scissors" and comp_list[x] == "paper":
        p1_score+= 1
    x += 1

print(f'\nscore of player 1: {p1_score}\nscore of computer: {co_score}')

# Final

if p1_score > co_score :
    print('Player 1 is the winner!')

elif p1_score == co_score :
    print('Draw!')
    
elif p1_score < co_score :
    print('computer is the winner!')


print(f"\ncomputers first choice: {co_1}")
print(f"computers second choice: {co_2}")
print(f"computers third choice: {co_3}")
