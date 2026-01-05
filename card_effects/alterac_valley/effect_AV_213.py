"""Effect for Vitality Surge (AV_213).

Card Text: Draw a minion.
Restore Health to your hero equal to its Cost.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)