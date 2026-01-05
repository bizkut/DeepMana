"""Effect for Ancient Pterrordax (TLC_246).

Card Text: [x]<b>Battlecry:</b> Choose to gain
<b>Stealth</b> until your next turn,
<b>Elusive</b>, or <b>Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass