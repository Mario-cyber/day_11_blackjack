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
    
# calculates score and replaces ace from 11 to 1 if score is > 21 

def calculate_score(hand):
      score = sum(hand)
      if score > 21 and 11 in hand:
          hand[hand.index(11)] = 1 
      score = sum(hand)
      return score


# fix this function so it works for both dealer and player 
def check_for_bust (score):
    
     if score > 21:
          print(f"you went over 21 you lose")
          return False
     else:
          return True 