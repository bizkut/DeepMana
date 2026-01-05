"""Effect for Frostmourne (RLK_086).

Card Text: <b>Deathrattle:</b> Summon every minion killed by this weapon.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_086t")