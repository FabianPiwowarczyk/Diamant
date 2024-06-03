from player import Player
from deck import Deck


class GameLoop:
    def __init__(self, config):
        self.players = [Player(name, config[name]) for name in config.keys()]
        self.config = config
        self.deck = Deck()
        self.roundCount = 1
        self.active_players = self.players[:]
        self.ground_gems = 0
        self.played_cards = []
        self.leaving_players = []

    def main_loop(self):
        for self.roundCount in range(1, 6):
            while self.active_players:
                card = self.deck.draw_card()
                # print('drawn card: ', card)
                # print(self.deck.deck_lst)
                # input('input')
                damage_calc = self.calc_card(card)
                if damage_calc:
                    self.player_decision()
                else:
                    # print('danger end')
                    self.round_end_danger()
                # for player in self.players:
                #     print(player.name, ' gems ', player.gems, ' vault ', player.vault)
                # print('leaving players: ', [player.name for player in self.leaving_players])
                # print('still active: ', [player.name for player in self.active_players])
            self.deck.update_deck()
            # print(self.deck.deck_lst)
            self.active_players = self.players[:]
            # print('active players reset: ', len(self.active_players))
            # print('played cards: ', self.played_cards)
            self.played_cards = []
            # print('played cards reset: ', self.played_cards)
            # for player in self.players:
            #     print(player.name, ' gems ', player.gems, ' vault ', player.vault)
            # print(self.roundCount)
            # input('input')
        print(self.round_win())

    def round_end_danger(self):
        for player in self.active_players:
            player.set_gems_zero()
        self.active_players = []
        self.deck.remove_danger(self.played_cards[-1])

    def player_decision(self):
        self.leaving_players = []
        for player in self.active_players:
            des = player.decision(self.__dict__)
            if not des:
                self.leaving_players.append(player)
        if self.leaving_players:
            self.calc_leaving()

    def calc_leaving(self):
        for player in self.leaving_players:
            self.active_players.remove(player)
        added_gems = self.ground_gems // len(self.leaving_players)
        self.ground_gems = self.ground_gems % len(self.leaving_players)
        for player in self.leaving_players:
            player.add_gems(added_gems)
            player.win_vault()

    def calc_card(self, card):
        if type(card) == int:
            added_gems = card // len(self.active_players)
            self.ground_gems += card % len(self.active_players)
            for player in self.active_players:
                player.add_gems(added_gems)
            self.played_cards.append(card)
            return True
        if type(card) == str:
            if card in self.played_cards:
                self.played_cards.append(card)
                return False
            else:
                self.played_cards.append(card)
                return True

    def round_win(self):
        winning_players = [[player.name, player.vault] for player in self.players if player.vault == max([player.vault for player in self.players])]
        return winning_players
