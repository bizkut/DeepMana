"""Effect for Maxima Blastenheimer (DMF_089).

Card Text: [x]<b>Battlecry:</b> Summon a minion
from your deck. It attacks the
enemy hero, then dies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_089t")