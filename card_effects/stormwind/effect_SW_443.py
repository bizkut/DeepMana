"""Effect for Elekk Mount (SW_443).

Card Text: Give a minion +4/+7 and <b>Taunt</b>. When it dies, summon an Elekk.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_443t")