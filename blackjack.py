import random
# genenerate deck

cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]

# generate variables to be populated

player_hand = []
dealer_hand = []

player_score = []
dealer_score = []


iterator = 0

while iterator < 2:
    player_hand.append(cards[random.randint(0,len(cards))])
    dealer_hand.append(cards[random.randint(0,len(cards))]) 
    iterator += 1

player_score = sum(player_hand)
dealer_score = sum(dealer_hand)

print(player_hand, player_score)
print(dealer_hand, dealer_score)
