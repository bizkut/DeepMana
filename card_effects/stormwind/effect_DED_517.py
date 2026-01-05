"""Effect for Arcane Overflow (DED_517).

Card Text: [x]Deal $8 damage to an
enemy minion. Summon a
 Remnant with stats equal
to the excess damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)