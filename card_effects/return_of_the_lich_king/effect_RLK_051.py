"""Effect for Vampiric Blood (RLK_051).

Card Text: [x]Give your hero +5 Health.
Spend 3 <b>Corpses</b> to gain
5 more and draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)