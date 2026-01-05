"""Effect for The Beast (EX1_577).

Card Text: [x]<b>Deathrattle:</b> Summon a
3/3 Pip Quickwit for
your opponent.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EX1_577t")