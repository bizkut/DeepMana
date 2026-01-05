"""Effect for Whirliglider (BOT_431).

Card Text: <b>Battlecry:</b> Summon a 0/2 Goblin Bomb.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_431t")