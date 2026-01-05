"""Effect for Lost Exarch (NX2_032).

Card Text: [x]<b>Deathrattle</b>: Spend all your
Mana. Summon that many
 2/2 Zombies with <b>Rush</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NX2_032t")