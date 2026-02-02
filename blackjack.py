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


print(f"your cards are: {player_hand} and your total is {player_score}")

print(f"the dealer is showing: {dealer_hand[0]}")



continue_playing =  True


while continue_playing == True:
    another_card = input("do you want another card? y/n: ")

    if another_card == 'y':
        # deal another card to player 
        moves.hit(hand=player_hand)
        player_score = moves.calculate_score(hand = player_hand)
        print(player_hand, player_score)
        continue_playing = moves.check_for_bust_player(score=player_score)
        if player_score == 21:
            print("you win, player!")
        
        
    elif another_card == 'n':
        print(player_hand, player_score)
        continue_playing  = False


#gotta split the loop here, otherwise, if the player busts, the dealer can still play 

#dealer only plays if the player has not bust 

if player_score > 21 :
    print("you lose")
else:
    while 17 > dealer_score:
        #deal another card to dealer
        moves.hit(hand = dealer_hand)
        dealer_score = moves.calculate_score(hand=dealer_hand) 
        print(dealer_hand,dealer_score)
        
    # comparison logic 
    if dealer_score > 21 : 
        print("dealer wnt over 21, you win!")
    else:
        print(f"final score: \n Player: {player_hand}-> {player_score} \nDealer: {dealer_hand} -> {dealer_score}")
        if dealer_score > player_score:
            print("you lose !")
        elif dealer_score < player_score:
            print("you win")
        else:
            print("it's a push")
