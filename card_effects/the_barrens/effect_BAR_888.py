"""Effect for Rimetongue (BAR_888).

Card Text: After you cast a Frost spell, summon a 1/1 Elemental that <b><b>Freeze</b>s</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_888t")