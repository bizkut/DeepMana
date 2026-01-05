"""Effect for Immolate (TID_718).

Card Text: Light every card in the opponent's hand on fire. In 3 turns, any still
in hand are destroyed!
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()