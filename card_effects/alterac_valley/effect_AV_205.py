"""Effect for Wildheart Guff (AV_205).

Card Text: [x]<b>Battlecry:</b> Set your
maximum Mana to 20.
Gain an empty Mana
Crystal. Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(20)