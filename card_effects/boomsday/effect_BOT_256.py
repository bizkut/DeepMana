"""Effect for Astromancer (BOT_256).

Card Text: [x]<b>Battlecry:</b> Summon a
random minion with Cost
equal to your hand size.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_256t")