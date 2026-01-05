"""Effect for Skycap'n Kragg (AT_070).

Card Text: <b>Charrrrrge</b>
Costs (1) less for each friendly Pirate.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass