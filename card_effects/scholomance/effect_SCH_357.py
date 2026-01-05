"""Effect for Fel Guardians (SCH_357).

Card Text: Summon three 1/2 Demons with <b>Taunt</b>. Costs (1) less whenever a friendly minion dies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_357t")