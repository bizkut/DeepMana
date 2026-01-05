"""Effect for Sparkjoy Cheat (YOP_016).

Card Text: <b>Battlecry:</b> If you're holding a <b>Secret</b>, cast it and draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)