"""Effect for Rocket Boots (BOT_067).

Card Text: Give a minion <b>Rush</b>. Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)