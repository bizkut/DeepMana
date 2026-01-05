"""Effect for Wicked Witchdoctor (WON_083).

Card Text: Whenever you cast a spell, summon a random basic Totem.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_083t")