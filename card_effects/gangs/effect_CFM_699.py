"""Effect for Seadevil Stinger (CFM_699).

Card Text: [x]<b>Battlecry:</b> The next Murloc
you play this turn costs
 Health instead of Mana.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)