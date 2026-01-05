"""Effect for Unholy Frenzy (RLK_056).

Card Text: [x]Choose an enemy minion.
Your minions attack it.
Resummon any that die.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_056t")