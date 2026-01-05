"""Effect for Possessed Animancer (DINO_131).

Card Text: [x]<b>Deathrattle:</b> Summon a
random Beast from your
deck. Give it <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_131t")