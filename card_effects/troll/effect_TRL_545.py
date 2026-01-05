"""Effect for Zandalari Templar (TRL_545).

Card Text: [x]<b>Battlecry:</b> If you've restored
10 Health this game, gain
+4/+4 and <b>Taunt</b>.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 10, source)