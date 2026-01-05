"""Effect for Final Gasp (WC_022).

Card Text: [x]Deal $1 damage to a
minion. If it dies, summon
a 2/2 Adventurer with a
random bonus effect.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)