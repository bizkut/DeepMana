"""Effect for Tanaris Hogchopper (CFM_809).

Card Text: [x]<b>Battlecry:</b> If your opponent's
hand is empty, gain <b>Charge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass