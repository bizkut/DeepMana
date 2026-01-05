"""Effect for Klaxxi Amber-Weaver (WON_010).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If your C'Thun
has at least 10 Attack,
gain +5 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 10, source)