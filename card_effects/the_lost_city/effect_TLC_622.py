"""Effect for City Defenses (TLC_622).

Card Text: Summon two 0/6 Security with <b>Taunt</b>.
They gain +1 Attack
when damaged.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_622t")