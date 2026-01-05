"""Effect for Pursuit of Justice (CS3_029).

Card Text: Give +1 Attack to Silver Hand Recruits you summon this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CS3_029t")