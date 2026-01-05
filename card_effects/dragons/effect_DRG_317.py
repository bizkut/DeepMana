"""Effect for Secure the Deck (DRG_317).

Card Text: <b>Sidequest:</b> Attack twice with your hero. <b>Reward:</b> Add 3 'Claw' spells to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass