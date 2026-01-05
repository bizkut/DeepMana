"""Effect for Plague of Madness (ULD_715).

Card Text: Each player equips
a 2/2 Knife with <b>Poisonous</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass