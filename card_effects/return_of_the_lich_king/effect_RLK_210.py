"""Effect for Wretched Exile (RLK_210).

Card Text: [x]After you play an <b>Outcast</b>
card, add a random <b>Outcast</b>
card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass