"""Effect for Cornered Sentry (UNG_926).

Card Text: <b>Taunt</b>. <b>Battlecry:</b> Summon three 1/1 Raptors for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_926t")