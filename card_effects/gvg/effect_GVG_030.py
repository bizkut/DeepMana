"""Effect for Anodized Robo Cub (GVG_030).

Card Text: <b>Taunt</b>. <b>Choose One -</b>
+1 Attack; or +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)