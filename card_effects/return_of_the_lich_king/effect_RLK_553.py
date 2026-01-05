"""Effect for Prescience (RLK_553).

Card Text: Draw 2 minions. For each that costs (5)
or more, summon a 
2/3 Spirit with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)