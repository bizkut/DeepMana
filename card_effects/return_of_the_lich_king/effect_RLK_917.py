"""Effect for Flight of the Bronze (RLK_917).

Card Text: [x]<b>Discover</b> a Dragon.
<b>Manathirst (7):</b> Summon
a 5/5 Drake with <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_917t")