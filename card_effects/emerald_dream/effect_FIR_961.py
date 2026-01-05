"""Effect for Ashleaf Pixie (FIR_961).

Card Text: <b>Battlecry:</b> If you're holding a spell that costs (5) or more, gain <b>Divine Shield</b> and <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass