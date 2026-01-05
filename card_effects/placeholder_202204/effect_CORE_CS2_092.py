"""Effect for Blessing of Kings (CORE_CS2_092).

Card Text: Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)