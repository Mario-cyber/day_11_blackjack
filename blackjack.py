import first_deal
# genenerate deck

# cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]

# generate variables to be populated

player_hand = []
dealer_hand = []

player_score = []
dealer_score = []

# deal first 2 cards

first_deal.first_deal(player_hand=player_hand, dealer_hand=dealer_hand)

player_score = sum(player_hand)
dealer_score = sum(dealer_hand)

print(player_hand, player_score)
print(dealer_hand, dealer_score)




    

if dealer_score == 21 :
    print("you lose")
elif player_score == 21 :
    print("you win")


