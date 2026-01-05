"""Effect for Lady in White (GIL_840).

Card Text: [x]<b>Battlecry:</b> Cast 'Inner Fire'
 on every minion in your deck 
<i>(set Attack equal to Health).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)