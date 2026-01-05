"""Effect for Sporegnasher (EDR_110).

Card Text: <b>Poisonous</b>
<b>Deathrattle:</b> Deal 1
damage to a random
enemy minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)