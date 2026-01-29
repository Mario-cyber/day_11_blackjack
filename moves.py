import random
cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]

# generate variables to be populated

def first_deal(player_hand, dealer_hand):
     iterator = 0 
    
     while iterator < 2:
     
        player_hand.append(cards[random.randint(0,len(cards)-1)])
        dealer_hand.append(cards[random.randint(0,len(cards)-1)])
        

        iterator += 1



def hit(hand):
    hand.append(cards[random.randint(0,len(cards)-1)])
    return hand
    

def calculate_score(hand):
      score = sum(hand)
      return score

# maybe do a function that allows the Ace to be 11 or 1...
""" put a library in the "cards" and if sum > 21 and 11 in set:
replace 11 with the 1 by searching for the value using the key """


# fix this function so it works for both dealer and player 
def check_for_bust (score):
    
     if score > 21:
          print(f"you went over 21 you lose")
          return False
     else:
          return True 