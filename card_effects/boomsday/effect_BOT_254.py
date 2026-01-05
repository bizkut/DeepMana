"""Effect for Unexpected Results (BOT_254).

Card Text: [x]Summon two random
$2-Cost minions <i>(improved
by <b>Spell Damage</b>)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BOT_254t")