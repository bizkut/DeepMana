"""Effect for Murloc Tidehunter (EX1_506).

Card Text: <b>Battlecry:</b> Summon a 1/1 Murloc Scout.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EX1_506t")