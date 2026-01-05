"""Effect for Instant Multiverse (TIME_014).

Card Text: <b>Rewind</b>
Summon 12 Mana worth of random minions.
<b>Overload:</b> (3)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_014t")