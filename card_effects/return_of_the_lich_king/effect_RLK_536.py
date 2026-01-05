"""Effect for Shallow Grave (RLK_536).

Card Text: Trigger a friendly minion's <b>Deathrattle</b>, then destroy it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()