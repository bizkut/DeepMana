"""Effect for Coppertail Imposter (BOT_562).

Card Text: <b>Battlecry:</b> Gain <b>Stealth</b> until your next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass