"""Effect for Masked Contender (TRL_530).

Card Text: <b>Battlecry:</b> If you control a <b>Secret</b>, cast a <b>Secret</b> from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass