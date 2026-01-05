"""Effect for Eversong Portal (RLK_819).

Card Text: [x]Summon $1 4/4 Lynxes
with <b>Rush</b> <i>(improved by
<b>Spell Damage</b>)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_819t")