"""Effect for Arcane Blast (AT_004).

Card Text: Deal $2 damage to a minion. This spell gets double bonus from <b>Spell Damage</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)