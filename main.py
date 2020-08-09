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

    def draw(self):
        self.money += self.bet_amount
        self.bet_amount = 0

    def has_black_jack(self):
        return (self.score == 21 and len(self.hand) == 2)

def print_house(house):
    house_copy = house.hand[:]
    house_copy[0] = 'X';
    print(f'House: {", ".join(house_copy)}')

card_deck = create_deck()
first_hand = [card_deck.pop(), card_deck.pop()]
second_hand = [card_deck.pop(), card_deck.pop()]
player1 = Player(first_hand)
house = Player(second_hand)
card_deck = create_deck()
while True:
    if len(card_deck) < 20:
        card_deck = create_deck()
    first_hand = [card_deck.pop(), card_deck.pop()]
    second_hand = [card_deck.pop(), card_deck.pop()]
    player1.play(first_hand)
    house.play(second_hand)
    bet = int(input('Please enter the amount you want to bet: '))
    if bet <= player1.money:
        player1.bet(bet)
    else:
        print(f'Entered amount is greater than the money in your wallet. Total money {player1.money}')
        continue
    print(card_deck)
    print_house(house)
    print(player1)

    if player1.has_black_jack():
        if house.has_black_jack():
            player1.draw()
            print('Game is draw as both player and house has a black jack')
            print(f'Total amount with player1 after the game: {player1.money}')
        else:
            player1.win(True)
            print('Player1 won the game, since it has black jack')
            print(f'Total amount with player1 after the game: {player1.money}')
    elif house.has_black_jack():
        player1.win(False)
        print('Player1 lost the game, house has a blackjack')
        print(f'Total amount with player1 after the game: {player1.money}')
    else:
        while(player1.score < 21):
            action = input('Do you want to pick another card?(y/n): ')
            if action.lower()[0] == 'y':
                player1.hit(card_deck.pop())
                print(f'Player1 {player1}')
                print_house(house)
            else:
                break

        while house.score < 16:
            house.hit(card_deck.pop())
            print_house(house)

        if player1.score > 21:
            if house.score > 21:
                player1.draw()
                print('Game is draw as both player and house had equal score')
                print(f'Total amount with player1 after the game: {player1.money}')
            else:
                player1.win(False)
                print(f'Player1 lost the game, house score was: {house.score}')
                print(f'Total amount with player1 after the game: {player1.money}')
        elif player1.score == house.score:
            player1.draw()
            print('Game is draw as both player and house had equal score')
            print(f'Total amount with player1 after the game: {player1.money}')
        elif player1.score > house.score:
            player1.win(True)
            print(f'Player1 won the game, house score was: {house.score}')
            print(f'Total amount with player1 after the game: {player1.money}')
        else:
            if house.score > 21:
                player1.win(True)
                print('Player1 won the game, house score was above 21')
                print(f'Total amount with player1 after the game: {player1.money}')
            else:
                player1.win(False)
                print(f'Player1 lost the game, house score was: {house.score}')
                print(f'Total amount with player1 after the game: {player1.money}')

    wants_to_continue = input('You want to continue playing?(y/n): ')
    if wants_to_continue.lower()[0] != 'y':
        break

print(f'Total amount with player 1 after the game: {player1.money}')