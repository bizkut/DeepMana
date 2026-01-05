"""Effect for Spikeridged Steed (CORE_UNG_952).

Card Text: Give a minion +2/+6 and <b>Taunt</b>. When it dies, summon a Stegodon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
