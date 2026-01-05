"""Effect for Story of Sulfuras (TLC_632).

Card Text: [x]Swap your Hero Power
to "Deal 8 damage
to a random enemy."
After 2 uses, swap back.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 8, source)