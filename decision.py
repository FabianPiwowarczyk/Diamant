def players_brain(name, game_state):

    players = dict()
    for player in game_state['players']:
        players[player.name] = player

    choosing_player = players.pop(name)
    opponent_players = players

    deck_lst = game_state['deck'].deck_lst
    deck_dia = game_state['deck'].dia
    deck_dng = game_state['deck'].dangers

    roundCount = game_state['roundCount']

    active_players = [player.name for player in game_state['active_players']]

    ground_gems = game_state['ground_gems']

    played_cards = game_state['played_cards']

    end_pos = danger_end_possibility(deck_lst, deck_dng, played_cards)

    decision = leave(end_pos, choosing_player)

    return decision


def danger_end_possibility(deck_lst, deck_dng, played_cards):
    dangers = [key for key in deck_dng.keys() if deck_dng[key] > 1]
    danger_count = len([danger for danger in dangers if danger in played_cards])
    end_pos = danger_count / len(deck_lst)
    return end_pos


def leave(end_pos, choosing_player):

    dng_coef = choosing_player.dng_coef

    leav_coef = end_pos * dng_coef

    return True if leav_coef < 1 else False


