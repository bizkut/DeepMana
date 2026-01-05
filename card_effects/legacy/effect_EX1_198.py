"""Effect for Natalie Seline (EX1_198).

Card Text: <b>Battlecry:</b> Destroy a minion and gain its Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()