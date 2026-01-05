"""Effect for Selfless Sidekick (WC_029).

Card Text: <b>Battlecry:</b> Equip a random weapon from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass