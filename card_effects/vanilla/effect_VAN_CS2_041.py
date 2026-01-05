"""Effect for Ancestral Healing (VAN_CS2_041).

Card Text: Restore a minion
to full Health and
give it <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)