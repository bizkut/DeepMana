"""Effect for Composting (SW_437).

Card Text: Give your minions
"<b>Deathrattle:</b> Draw
  a card."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)