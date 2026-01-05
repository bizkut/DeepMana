"""Effect for Ramming Mount (SW_458).

Card Text: [x]Give a minion +2/+2
and <b>Immune</b> while
attacking. When it dies,
summon a Ram.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_458t")