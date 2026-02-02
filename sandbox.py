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

# after funcionality is done, fix this display to only one card
# print(dealer_hand[0])
print(dealer_hand, dealer_score)

# check for blackjack
# it could be the case that both player and dealer hit blackjack in the first deal. That's a push. 
# check for dealer blackjack first if the dealer is under 

continue_playing =  True

# you will have to fix this later to give the dealer or player a chance to "push"
if dealer_score == 21 :
    print("you lose")
    continue_playing = False
elif player_score == 21 :
    print("you win")
    continue_playing = False



while continue_playing == True:
    another_card = input("do you want another card? y/n: ")

    if another_card == 'y':
        # deal another card to player 
        moves.hit(hand=player_hand)
        player_score = moves.calculate_score(hand = player_hand)
        print(player_hand, player_score)
        continue_playing = moves.check_for_bust_player(score=player_score)
        print(f"here is what is ahppening here: continue_playing = {continue_playing}")
        if player_score == 21:
            #if you hit 21 you don't immediatly win becasue the 
            #dealer can still try to tie (push)
            #also, the user is allowed to hit at 21 if they want ot be stupid enough 
            print("dealer can still draw")

        
    elif another_card == 'n':
        print(player_hand, player_score)
        continue_playing  = False


# If the player busted, don't let the dealer play
if player_score > 21:
    # `moves.check_for_bust_player` already prints a message when player busts,
    # but make the outcome explicit here as well
    print("You went over 21. Dealer wins.")
else:
    # Dealer draws until reaching 17 or higher (standard rule)
    while dealer_score < 17:
        moves.hit(hand=dealer_hand)
        dealer_score = moves.calculate_score(hand=dealer_hand)
        print(dealer_hand, dealer_score)

    # Determine final outcome
    if dealer_score > 21:
        print("Dealer went over 21. You win! ✅")
    else:
        print(f"Final hands:\nPlayer: {player_hand} -> {player_score}\nDealer: {dealer_hand} -> {dealer_score}")
        if dealer_score > player_score:
            print("You lose 😞")
        elif dealer_score < player_score:
            print("You win! 🎉")
        else:
            print("It's a push (tie).")

#remainig To Do's: 
#display only one of the dealers hands at the begining of the game 
#fix check for bust option so that the right message is displayed