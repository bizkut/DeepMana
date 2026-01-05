"""Effect for C'Thun (WON_135).

Card Text: <b>Battlecry:</b> Deal damage
equal to this minion's
Attack randomly split among all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)