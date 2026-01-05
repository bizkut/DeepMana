"""Effect for Plagued Grain (LEG_RLK_039).

Card Text: Gain 4 <b>Corpses</b>. Shuffle four Crates into your deck that summon a 2/2 Undead when drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)