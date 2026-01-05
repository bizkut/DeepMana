"""Effect for Crystal Broker (RLK_221).

Card Text: [x]<b>Manathirst (5):</b> Summon a
random 3-Cost minion.
<b>Manathirst (10):</b> Summon an
8-Cost minion instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_221t")