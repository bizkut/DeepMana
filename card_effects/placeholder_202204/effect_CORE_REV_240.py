"""Effect for Tome Tampering (CORE_REV_240).

Card Text: [x]Shuffle 1-Cost 
copies of cards in your 
hand into your deck, 
then discard your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass