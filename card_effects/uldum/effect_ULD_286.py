"""Effect for Shadow of Death (ULD_286).

Card Text: Choose a minion. Shuffle 3 'Shadows' into your deck that summon a copy when drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)