import random

#card class
    #represent ONE card
    #attributes:
        #suit
        #value

#deck class
    #hold 52 card objects
    #attributes: --what can we use to hold a list of cards?-- array
        #deck(array)

#player class
    #interact with the cards and/or the deck in some sort of way
    #attributes
        #name
        #hand(array)

class Card(object): #class card inherits from the base object class
    def __init__(self, value, suit): #this is known as the constructor function
        #any code that we write here will be executed as soon as we create a card.
        #you can assign attributes and you can also run methods here 
        self.suit = suit
        self.value = value 


card1 = Card("Ace", "Spades") #instantiated the class
#print "we have the {} of {}".format(card1.value, card1.suit) #card1 has access to those properties b/c card1 is an instance of the Card class

#print card1 #<__main__.Card object at 0x103687610>


class Deck():#does the deck need to inherit from a Card class....aka does a deck have a suit and a value? No, so we just pass in the object which is what we inherit from. its taking the base object
    def __init__(self): #b/c every class needs it, i'll need the init function with self passed into it.
        #create some attributes. We know we need a deck and it needs to be an array
        self.deck = [] #deck is an empty array that can hold 52 card objects.
        #if i want a single action, like pushing to an array, what do i need? a for loop!
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        values = [2,3,4,5,6,7,8,9,10,'Jack', 'King', 'Queen', 'Ace']
        #the loop should go to hearts, then run entirely through vlaues. Then go to diamonds, and go entirely through values. etc; --> thus we need a nested for loop

        for suit in suits:
            for value in values:  #since this is nested, we know that this iteration will complete for each iteration of the outer loop
                self.deck.append(Card(value, suit)) #append into the deck array the instance of the card class
        
    def shuffle(self):
        random.shuffle(self.deck)
        #fischer-yates shuffle is good shuffle to check out
        
a = Deck()
print a.deck #prints an array that has a  bunch of objects for each card. looks ugly so we run the code below to make it more readable. [{object}{object}{object}{object}]
a.shuffle()
for card in a.deck:
    print "{} of {}".format(card.value, card.suit)


class Player(object): #does player inherit any properties or methods from deck or card? No so we just pass in object as the base object it inherits from.
    def __init__(self, name):
        self.name = name
        self.hand = []
        #now we have a player that can interact with the deck of cards
    
         
    


