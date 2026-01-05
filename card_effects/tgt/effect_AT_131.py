"""Effect for Eydis Darkbane (AT_131).

Card Text: Whenever <b>you</b> target this minion with a spell, deal 3 damage to a random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)