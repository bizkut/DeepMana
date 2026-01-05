"""Effect for Shockspitter (RLK_825).

Card Text: <b>Battlecry:</b> Deal 1 damage.
<i>(Improved by your hero attacks this game!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)