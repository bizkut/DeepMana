"""Effect for Blast Wave (TRL_317).

Card Text: Deal $2 damage to all minions.
<b>Overkill</b>: Add a random Mage spell to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)