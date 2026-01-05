"""Effect for Ancient of War (EX1_178).

Card Text: <b>Choose One -</b>
+5 Attack; or +5 Health and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)