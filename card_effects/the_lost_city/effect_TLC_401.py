"""Effect for Bonechill Stegodon (TLC_401).

Card Text: <b>Deathrattle:</b> Deal
6 damage to three
random enemies.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 6, source)