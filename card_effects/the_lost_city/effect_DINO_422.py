"""Effect for Ankylodon (DINO_422).

Card Text: [x]<b><b>Taunt</b>. Deathrattle:</b> Summon
two random 3-Cost Beasts.
 They attack random enemies. 
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_422t")