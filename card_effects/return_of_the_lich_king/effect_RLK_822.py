"""Effect for Haunting Nightmare (RLK_822).

Card Text: [x]<b>Deathrattle:</b> Haunt a card in
your hand. When you play it,
summon a 4/3 Soldier.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_822t")