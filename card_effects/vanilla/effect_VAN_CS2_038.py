"""Effect for Ancestral Spirit (VAN_CS2_038).

Card Text: Choose a minion. When that minion is destroyed, return it to the battlefield.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()