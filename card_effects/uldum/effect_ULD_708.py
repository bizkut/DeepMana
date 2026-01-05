"""Effect for Livewire Lance (ULD_708).

Card Text: After your hero attacks, add a <b>Lackey</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass