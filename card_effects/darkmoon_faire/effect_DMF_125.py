"""Effect for Safety Inspector (DMF_125).

Card Text: [x]<b>Battlecry:</b> Shuffle the
 lowest-Cost card from
 your hand into your
 deck. Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)