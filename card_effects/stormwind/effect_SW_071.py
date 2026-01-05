"""Effect for Lion's Guard (SW_071).

Card Text: [x]<b>Battlecry:</b> If you have 15
or less Health, gain
+2/+4 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 15, source)