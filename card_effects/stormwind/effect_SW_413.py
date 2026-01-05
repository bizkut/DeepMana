"""Effect for SI:7 Operative (SW_413).

Card Text: <b>Rush</b>
After this attacks a minion, gain <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass