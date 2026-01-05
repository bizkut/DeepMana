"""Effect for Bloodscent Vilefin (TSC_753).

Card Text: [x]<b>Battlecry:</b> <b>Dredge</b>. If it's a
Murloc, change its Cost to
 Health instead of Mana.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)