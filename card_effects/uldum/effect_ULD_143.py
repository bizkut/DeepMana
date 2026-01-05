"""Effect for Pharaoh's Blessing (ULD_143).

Card Text: Give a minion +4/+4, <b>Divine Shield</b>, and <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4