"""Effect for The Black Knight (EX1_002).

Card Text: <b>Tradeable</b>
 <b>Battlecry:</b> Destroy an  enemy minion with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()