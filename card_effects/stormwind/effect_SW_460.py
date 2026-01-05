"""Effect for Devouring Swarm (SW_460).

Card Text: [x]Choose an enemy minion.
Your minions attack it,
then return any that die
 to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass