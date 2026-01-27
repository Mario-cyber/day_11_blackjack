import random
cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]

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


def check_for_bust (score):
     if score > 21:
          print("you lose")