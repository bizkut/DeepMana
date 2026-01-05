"""Effect for Hooded Acolyte (OG_334).

Card Text: [x]<b>Taunt</b>
Whenever a character is
healed, give your C'Thun
+1/+1 <i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)