from random import shuffle

def create_deck():
    deck = []
    suits = ['♠', '♡', '♢', '♣']
    face_cards = ['A', 'J', 'Q', 'K']
    for suit in suits:
        for card in range(2, 11):
            deck.append(f'{card}{suit}')
        for face in face_cards:
            deck.append(f'{face}{suit}')
    shuffle(deck)
    return deck

class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.bet_amount = 0

    def __str__(self):
        return (f'Current hand: {", ".join(self.hand)} Score: {self.score}')

    def set_score(self):
        self.score = 0
        face_dict = {'A':11, 'J':10, 'Q':10, 'K':10}
        ace_counter = 0
        for card in self.hand:
            if card[0] in face_dict:
                self.score += face_dict[card[0]]
                if card[0] == 'A':
                    ace_counter += 1
            elif int(card[0]) in range(2, 11):
                self.score += int(card[0])
            if self.score > 21 and ace_counter != 0:
                self.score -= 10
                ace_counter -= 1
        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.set_score()

    def play(self, new_hand):
        self.hand = new_hand
        self.score = self.set_score()

    def bet(self, amount):
        self.money -= amount
        self.bet_amount += amount

    def win(self, result):
        if result:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5 * self.bet_amount
            else:
                self.money += 2 * self.bet_amount
        self.bet_amount = 0

def print_house(house):
    house_copy = house.hand[:]
    house_copy[0] = 'X';
    print(f'{", ".join(house_copy)}')

card_deck = create_deck()
first_hand = [card_deck.pop(), card_deck.pop()]
second_hand = [card_deck.pop(), card_deck.pop()]
player1 = Player(first_hand)
house = Player(second_hand)
print(card_deck)
print_house(house)
print(player1)

while(player1.score < 21):
    action = input('Do you want to pick another card?(y/n): ')
    if action.lower()[0] == 'y':
        player1.hit(card_deck.pop())
        print(player1)
        print_house(house)
    else:
        break
