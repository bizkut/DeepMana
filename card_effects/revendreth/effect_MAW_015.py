"""Effect for Jury Duty (MAW_015).

Card Text: [x]Summon two
Silver Hand Recruits.
Give your Silver Hand
Recruits +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "MAW_015t")