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

card_deck = create_deck()
print(card_deck)

class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.set_score()
        self.money = money

    def __str__(self):
        return (f'Current hand: {",".join(self.hand)} Score: {self.score}')

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

        def pay(self, amount):
            self.money -= amount

        def win(self, amount):
            self.money += amount

player1 = Player(['3♣', '7♠', '5♢'], 200)
player1.hit('K♢')
player1.pay(20)
player1.win(40)
player1.play(['A♠', 'K♢'])
print(player1)
print(player1.money)
