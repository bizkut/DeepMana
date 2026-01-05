"""Effect for Whirlkick Master (ULD_231).

Card Text: Whenever you play a <b>Combo</b> card, add a random <b>Combo</b> card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass