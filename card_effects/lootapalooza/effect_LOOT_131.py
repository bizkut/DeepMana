"""Effect for Green Jelly (LOOT_131).

Card Text: At the end of your turn, summon a 1/2 Ooze with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_131t")