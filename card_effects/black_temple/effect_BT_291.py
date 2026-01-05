"""Effect for Apexis Blast (BT_291).

Card Text: Deal $5 damage.
If your deck has no minions, summon a random 5-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 5, source)