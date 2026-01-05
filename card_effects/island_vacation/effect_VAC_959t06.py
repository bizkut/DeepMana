"""Effect for Amulet of Critters (VAC_959t06).

Card Text: Summon a random 4-Cost minion and give it <b>Taunt</b>. <i>(It can't attack!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
