# sanbox to play around 

import random
# genenerate deck

cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]

# generate variables to be populated

player_hand = []
dealer_hand = []

player_score = 0
dealer_score = 0

counter = 0

def first_deal(player_hand, dealer_hand,player_score, dealer_score):
     iterator = 0 
    
     while iterator < 2:
     
        player_hand.append(cards[random.randint(0,len(cards)-1)])
        dealer_hand.append(cards[random.randint(0,len(cards)-1)])
        

        iterator += 1



# del first 2 cards

while player_score != 21 :
    
    first_deal(player_hand=player_hand, dealer_hand=dealer_hand, player_score=player_score, dealer_score=dealer_score)
   
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    print(player_hand, player_score)
    print(dealer_hand, dealer_score)

    player_hand =[]
    dealer_hand = []
    counter += 1
    
print("you hit 21 ! you win")
print(f"it took you {counter} attempts!")



    

# if dealer_score == 21 :
#     print("you lose")
# elif player_score == 21 :
#     print("you win")


