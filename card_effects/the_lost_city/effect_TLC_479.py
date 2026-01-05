"""Effect for Deathrot Maw (TLC_479).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Summon a random Fel Beast.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_479t")