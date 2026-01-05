"""Effect for Catacomb Guard (SW_317).

Card Text: [x]<b>Lifesteal</b>
<b>Battlecry:</b> Deal damage
equal to this minion's Attack
to an enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)