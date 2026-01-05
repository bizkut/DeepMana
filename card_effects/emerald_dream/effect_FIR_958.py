"""Effect for Tindral Sageswift (FIR_958).

Card Text: [x]<b>Deathrattle:</b> Deal 1 damage
to all enemies. If it's your
opponent's turn, deal
4 damage instead.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)