"""Effect for Lightmender (EDR_257).

Card Text: [x]<b><b>Taunt</b>.</b> <b>Choose One -</b>
+3 Attack and <b>Divine Shield</b>;
 or +3 Health and <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)