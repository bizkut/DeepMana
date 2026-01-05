"""Effect for Giggling Inventor (BOT_270).

Card Text: <b>Battlecry:</b> Summon two 1/2 Mechs with <b>Taunt</b> and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_270t")