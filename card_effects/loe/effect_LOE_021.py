"""Effect for Dart Trap (LOE_021).

Card Text: <b>Secret:</b> After an opposing Hero Power is used, deal $5 damage to a random enemy.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 5, source)