"""Effect for Aranasi Broodmother (DAL_185).

Card Text: [x]<b>Taunt</b>
When you draw this, restore
#4 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)