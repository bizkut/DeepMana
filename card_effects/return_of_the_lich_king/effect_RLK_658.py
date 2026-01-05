"""Effect for Elder Nadox (RLK_658).

Card Text: <b>Battlecry:</b> Destroy a friendly Undead. Your minions gain its Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()