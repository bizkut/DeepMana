"""Effect for Azsharan Mooncatcher (TSC_644).

Card Text: [x]<b>Divine Shield</b>. <b>Battlecry:</b> Put
a 'Sunken Mooncatcher' on
the bottom of your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass