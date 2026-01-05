"""Effect for E.M.P. Operative (BOT_540).

Card Text: <b>Battlecry:</b> Destroy a Mech.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()