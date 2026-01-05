"""Effect for Ambush Predators (TLC_519).

Card Text: Summon a 1/1 Spitter with <b>Stealth</b>
and <b>Poisonous</b>.
<b>Kindred:</b> Do it again.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_519t")