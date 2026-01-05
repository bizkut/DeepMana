"""Effect for Security Rover (BOT_218).

Card Text: [x]Whenever this minion
takes damage, summon a
2/3 Mech with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_218t")