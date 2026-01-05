"""Effect for Fjola Lightbane (AT_129).

Card Text: Whenever <b>you</b> target this minion with a spell, gain <b><b>Divine Shield</b>.</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass