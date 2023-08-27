############### Blackjack Project #####################
#Zachary Sheppard
#August 27, 2023

import random
import art
from replit import clear

#List represents possible values in card deck
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#Start of game deals cards to player and dealer
def start():
  user_cards = []
  dealer_cards = []

  #Dealing starting hand for player
  for x in range(0,2):
    user_cards.append(random.choice(deck))
  hand = sum(user_cards)
  
  #Dealing starting hand for dealer
  dealer_cards.append(random.choice(deck))
  
  print(f"Your cards: {user_cards}, current score: {hand}")
  print(f"Computer's first card: {dealer_cards}")

  return user_cards, dealer_cards

#Function deals player cards and prints card hands
def hit(user_cards, dealer_cards):
  user_cards.append(random.choice(deck))
  user_hand = sum(user_cards)
  print(f"Your cards: {user_cards}, current score: {user_hand}")
  print(f"Computer's first card: {dealer_cards}")
  return user_cards

#Dealer plays cards until over 17
def dealer_hit(dealer_cards):

  while sum(dealer_cards) < 17:
    dealer_cards.append(random.choice(deck))
    if sum(dealer_cards) > 21 and 11 in dealer_cards:
      dealer_cards.remove(11)
      dealer_cards.append(1)
      
  return dealer_cards
  
#Function for Checking win conditions
def tally(user_cards, dealer_cards):
  print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
  print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")

  if sum(user_cards) == sum(dealer_cards) and sum(user_cards) < 22:
    return "Draw!"
  elif sum(user_cards) > 21 and len(user_cards) == 2:
    return "BLACKJACK. You win!"
  elif sum(user_cards) > 21:
    return "You went over. You lose!"
  elif sum(dealer_cards) > 21:
    return "Dealer went over. You win!"
  elif sum(user_cards) > sum(dealer_cards):
    return "You win!"
  elif sum(dealer_cards) > sum(user_cards):
    return "You lose!"

#Ask user if they want to play
user_continue = input("Do you want to play a game of Blackjack? 'y' or 'n': ")

if user_continue == 'y':
  exit_game = False

  #Start of Blackjack game
  while not exit_game:
    clear()
    print(art.logo)
    exit_blackjack = False
    user_hand, dealer_hand = start()

    #User Hits or Passes
    while not exit_blackjack:
      user_move = input("Type 'y' to get another card, type 'n' to pass: ")
  
      if user_move == 'y':
        user_hand = hit(user_hand, dealer_hand)

        if sum(user_hand) > 21 and len(user_hand) == 2:
          dealer_hand = dealer_hit(dealer_hand)
          print(tally(user_hand, dealer_hand))
          exit_blackjack = True
        
        if sum(user_hand) > 21 and 11 in user_hand:
          user_hand.remove(11)
          user_hand.append(1)
          print("You went over but your ace (11) now turns into 1")
          print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
          print(f"Computer's first card: {dealer_hand}")
          
        if sum(user_hand) > 21:
          dealer_hand = dealer_hit(dealer_hand)
          print(tally(user_hand, dealer_hand))
          exit_blackjack = True
          
      else:
        dealer_hand = dealer_hit(dealer_hand)
        print(tally(user_hand, dealer_hand))
        exit_blackjack = True

    #Ask user if they want to play another game
    user_continue = input("Do you want to play a game of Blackjack? 'y' or 'n': ")
    if user_continue == 'n':
      exit_game = True
  
