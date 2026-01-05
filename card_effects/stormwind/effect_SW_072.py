"""Effect for Rustrot Viper (SW_072).

Card Text: [x]<b>Tradeable</b>
<b>Battlecry:</b> Destroy your
opponent's weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()