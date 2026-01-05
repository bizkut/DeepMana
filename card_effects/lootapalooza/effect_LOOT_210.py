"""Effect for Sudden Betrayal (LOOT_210).

Card Text: <b>Secret:</b> When a minion attacks your hero, instead it attacks one of its neighbors.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass