"""Effect for Raiding Party (CORE_TRL_124).

Card Text: Draw 2 Pirates from your deck.
<b>Combo:</b> And a weapon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)