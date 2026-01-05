"""Effect for Revenant Rascal (DMF_115).

Card Text: <b>Battlecry:</b> Destroy a Mana Crystal for each player.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()