hand  = [11,2,3,4,5,6]

print(hand)

if 11 in hand :
    print(hand.index(11))
    hand[hand.index(11)] = 1 
    print(hand)
    print(hand[0])