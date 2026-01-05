"""Effect for Theft Accusation (CORE_MAW_023).

Card Text: [x]Choose a minion.
Destroy it after you play
a card copied from
the opponent.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()