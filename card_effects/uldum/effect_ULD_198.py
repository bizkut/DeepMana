"""Effect for Conjured Mirage (ULD_198).

Card Text: <b>Taunt</b>
At the start of your turn, shuffle this minion into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass