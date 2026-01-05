"""Effect for Frost Lich Jaina (ICC_833).

Card Text: [x]<b>Battlecry:</b> Summon a
3/6 Water Elemental.
Your Elementals have
<b>Lifesteal</b> this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_833t")