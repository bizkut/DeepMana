"""Effect for Devouring Ectoplasm (WC_027).

Card Text: [x]<b>Deathrattle:</b> Summon a
2/2 Adventurer with
 a random bonus effect.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WC_027t")