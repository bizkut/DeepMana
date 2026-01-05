"""Effect for Lightforged Crusader (DRG_231).

Card Text: [x]<b>Battlecry:</b> If your deck has
no Neutral cards, add 5
random Paladin cards
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass