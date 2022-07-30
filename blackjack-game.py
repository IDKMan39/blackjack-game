import random
import time
FirstPlayerGone = False
bothlost = False


cardlist = ['ACE', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']
suitlist = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
sorteddeck = []
shuffleddeck = []
player1hand = []
player2hand = []
FirstPlayerGone = False
secondplayergone = False

numbers=[]
a_or_an = 'a'
cardvalue = 0
aceisout = False
m = 0
x = 0
def sort():

    if len(sorteddeck) < 52 :
        for eachcard in cardlist :
            for eachsuit in suitlist :
                card = eachcard + ' of ' + eachsuit
                sorteddeck.append(card)

# above is the creation of the sorteddeck
# below is the shuffleing
    while len(sorteddeck) >= 1 :
        amountcards = len(sorteddeck) - 1
        randpick = (random.randint(0, amountcards))
        appendcard = sorteddeck.pop(randpick)
        shuffleddeck.append(appendcard)

def bustfunction(dealer=False):
    if dealer :
        print("The dealer Busts")
    else :
        print("You Bust")
class playerclass :
    def __init__(self, hand, dealer=False) :
        self.hand = hand
        self.dealer = dealer
    def count(self) :

        cardvalue = 0
        twotonine = [ "", 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten' ]

        for eachcard in self.hand :
            number,of,suit = eachcard.split(' ')
            numbers.append(number)



            for eachnumber in twotonine :

                    if eachnumber == number :


                        cardvalue += twotonine.index(number) + 1


            if number == 'King' or number == 'Jack' or number == 'Queen' :
                cardvalue += 10


            if number == "ACE" and not self.dealer:

                acevalue = input(f"What would you like your {eachcard} to be \n \t > ")

                if acevalue == "11" or acevalue == "eleven" :
                    cardvalue += 11





                elif acevalue == 1 or acevalue == 'one':
                    cardvalue += 1
            elif number == "ACE" and self.dealer :
                if cardvalue+11 > 17 and cardvalue+11 < 21:
                    cardvalue += 11
                else :
                    cardvalue += 1






        return cardvalue
    def hitfunc(self):
        print(f"you have a {self.hand}")
        HitorPass = input("hit or stay > ")


        if HitorPass == 'hit' :
            nextcard = shuffleddeck.pop(0)
            self.hand.append(nextcard)
            print(f'Now you got a {nextcard} \n')




            if playerclass(self.hand).count() > 21 :
                bustfunction()
                return 0
            elif playerclass(self.hand).count() == 21 :
                print("you win wow \n")
                return 21
            playerclass(self.hand).hitfunc()


        elif HitorPass == "stay" :

            if playerclass(self.hand).count() > 21 :
                bustfunction()
                return 0
            elif playerclass(self.hand).count() < 21 :
                print(f"you got a {playerclass(self.hand).count()} \n")
            elif playerclass(self.hand).count() == 21 :
                print("you win wow \n" )
                return 21


        elif HitorPass == 'q' :
            exit()
        else :
            print("thats not a hit or stay")
            print("Again\n")
            time.sleep(.5)
            playerclass(self.hand).hitfunc()
        return playerclass(self.hand).count()
    def dealerf(self):
        print(f"Dealer has a {self.hand}\n")
        if playerclass(self.hand).count() > 21 :
            bustfunction(True)
            return 0


        if playerclass(self.hand).count() < 17 :
            nextcard = shuffleddeck.pop(0)
            self.hand.append(nextcard)
            print(f'The dealer got a {nextcard} \n')
            playerclass(self.hand).dealerf()
        else :
            print("The dealer stays")
        return playerclass(self.hand).count()











#s
sort()

##creates hand##
bothand = []
while m < 2 :
    bothandcards = shuffleddeck.pop(0)
    firsttwocards = shuffleddeck.pop(0)
    bothand.append(bothandcards)
    player1hand.append(firsttwocards)

    m =  m + 1
p = playerclass(player1hand).hitfunc()
d = playerclass(bothand).dealerf()
if p > d  :
    print("Player Wins")
elif d > p  :
    print("Dealer Wins")
else :
    print("both bust")
