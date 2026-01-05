"""Effect for Asphyxiodon (DINO_132).

Card Text: [x]<b>Taunt</b>. At the end of your
turn, deal 5 damage to a
random enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 5, source)