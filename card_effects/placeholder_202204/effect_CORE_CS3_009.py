"""Effect for War Cache (CORE_CS3_009).

Card Text: Add a random Warrior minion, spell, and weapon to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass