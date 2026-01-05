"""Effect for Foul Egg (RLK_833).

Card Text: <b>Deathrattle:</b> Summon a 3/3 Undead Chicken.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_833t")