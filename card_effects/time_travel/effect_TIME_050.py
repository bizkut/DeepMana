"""Effect for Sentient Hourglass (TIME_050).

Card Text: [x]<b>Rush</b>
After this minion survives
damage, swap its stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass