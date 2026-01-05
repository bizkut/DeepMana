"""Effect for Dragonbane Shot (ONY_010).

Card Text: [x]Deal $2 damage.
<b>Honorable Kill:</b> Add a 
Dragonbane Shot
to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)