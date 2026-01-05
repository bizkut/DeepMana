"""Effect for Jade Blossom (CFM_713).

Card Text: Summon a{1} {0} <b>Jade Golem</b>. Gain an empty Mana Crystal.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_713t")