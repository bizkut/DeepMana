"""Effect for Spreading Plague (CORE_ICC_054).

Card Text: Summon a 1/5 Scarab with <b>Taunt</b>. If your opponent has more minions, cast this again.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_054t")