"""Effect for Veteran Warmedic (BAR_878).

Card Text: [x]After you cast a Holy spell,
summon a 2/2 Medic
with <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_878t")