"""Effect for Explorer's Hat (LOE_105).

Card Text: Give a minion +1/+1 and "<b>Deathrattle:</b> Get an Explorer's Hat."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1