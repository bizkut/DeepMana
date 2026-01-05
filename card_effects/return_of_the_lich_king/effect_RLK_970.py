"""Effect for Hawkstrider Rancher (RLK_970).

Card Text: [x]Whenever you play a 
minion, give it +1/+1 and
"<b>Deathrattle:</b> Summon a 
1/1 Hawkstrider."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_970t")