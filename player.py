from decision import players_brain


class Player:
    def __init__(self, name):
        self.name = name
        self.vault = 0
        self.gems = 0

    def win_vault(self):
        self.vault += self.gems
        self.set_gems_zero()

    def add_gems(self, gems):
        self.gems += gems

    def set_gems_zero(self):
        self.gems = 0

    def decision(self):
        return players_brain(self.name)
