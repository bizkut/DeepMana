"""Effect for Mecha'thun (BOT_424).

Card Text: [x]<b>Deathrattle:</b> If you have no
cards in your deck, hand,
and battlefield, destroy
the enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()