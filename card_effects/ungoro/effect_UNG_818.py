"""Effect for Volatile Elemental (UNG_818).

Card Text: <b>Deathrattle:</b> Deal 3 damage to a random enemy minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)