"""Effect for Ice Walker (ICC_068).

Card Text: Your Hero Power also <b><b>Freeze</b>s</b> the target.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True