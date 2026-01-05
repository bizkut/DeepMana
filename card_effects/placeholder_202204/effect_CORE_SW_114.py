"""Effect for Overdraft (CORE_SW_114).

Card Text: [x]<b>Tradeable</b>
Unlock your <b>Overloaded</b>
Mana Crystals to deal
that much damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)