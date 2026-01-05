"""Effect for Ghastly Gravedigger (REV_959).

Card Text: [x]<b>Battlecry:</b> If you control a
<b>Secret</b>, choose a card in
your opponent's hand to
 shuffle into their deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass