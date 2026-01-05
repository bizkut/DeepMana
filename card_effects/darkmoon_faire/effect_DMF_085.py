"""Effect for Darkmoon Tonk (DMF_085).

Card Text: <b>Deathrattle:</b> Fire four  missiles at random enemies that deal 2 damage each.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)