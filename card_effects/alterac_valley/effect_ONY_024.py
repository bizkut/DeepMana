"""Effect for Onyxian Drake (ONY_024).

Card Text: [x]<b>Taunt</b>
 <b>Battlecry:</b> Deal damage
equal to your Armor to
an enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)