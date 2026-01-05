"""Effect for Bane of Doom (EX1_320).

Card Text: Deal $3 damage to a character. If that kills it, summon a random Demon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)