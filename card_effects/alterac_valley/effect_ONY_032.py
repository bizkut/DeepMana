"""Effect for Tooth of Nefarian (ONY_032).

Card Text: [x]Deal $3 damage.
<b>Honorable Kill:</b> <b>Discover</b> a
spell from another class.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)