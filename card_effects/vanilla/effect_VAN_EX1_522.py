"""Effect for Patient Assassin (VAN_EX1_522).

Card Text: <b>Stealth</b>. Destroy any minion damaged by this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()