import moves

# generate variables to be populated

player_hand = []
dealer_hand = []

player_score = []
dealer_score = []

# deal first 2 cards

moves.first_deal(player_hand=player_hand, dealer_hand=dealer_hand)

player_score = sum(player_hand)
dealer_score = sum(dealer_hand)

print(player_hand, player_score)
print(dealer_hand, dealer_score)

# check for blackjack
# it could be the case that both player and dealer hit blackjack in the first deal. That's a push. 
# check for dealer blackjack first if the dealer is under 

if dealer_score == 21 :
    print("you lose")
elif player_score == 21 :
    print("you win")

# continue game logic

continue_playing =  True

while continue_playing == True:
    another_card = input("do you want another card? y/n: ")

    if another_card == 'y':
        # deal another card to player 
        moves.hit(hand=player_hand)
        player_score = sum(player_hand)
        print(player_hand, player_score)
        
    elif another_card == 'n':
        print(player_hand, player_score)
        continue_playing  = False


