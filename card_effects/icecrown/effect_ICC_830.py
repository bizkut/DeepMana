"""Effect for Shadowreaper Anduin (ICC_830).

Card Text: <b>Battlecry:</b> Destroy all minions with 5 or more Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()