"""Effect for Frostwolf Kennels (AV_360).

Card Text: [x]At the end of your
turn, summon a 2/2
Wolf with <b>Stealth</b>.
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_360t")