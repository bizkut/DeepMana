"""Effect for Omega Agent (BOT_536).

Card Text: [x]<b>Battlecry:</b> If you have 10
Mana Crystals, summon
 2 copies of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_536t")