import random


class Deck:
    def __init__(self):
        self.dia = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
        self.dangers = {
                'snake': 3,
                'rocks': 3,
                'poison': 3,
                'scorpion': 3,
                'explosion': 3
                    }
        self.deck_lst = []
        self.update_deck()

    def update_deck(self):
        self.deck_lst = self.dia + [key for key in self.dangers.keys() for i in range(self.dangers[key])]

    def draw_card(self):
        card = random.choice(self.deck_lst)
        self.deck_lst.remove(card)
        return card

    def remove_danger(self, card):
        self.dangers[card] = self.dangers[card] - 1