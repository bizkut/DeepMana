"""Effect for Cleansing Lightspawn (TIME_427).

Card Text: [x]<b>Lifesteal</b>
<b>Battlecry:</b> Deal damage
to an enemy minion equal
   to this minion's Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)