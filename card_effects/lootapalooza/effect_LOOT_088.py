"""Effect for Potion of Heroism (LOOT_088).

Card Text: Give a minion <b>Divine Shield</b>.
Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)