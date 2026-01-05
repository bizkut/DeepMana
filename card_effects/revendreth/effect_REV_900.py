"""Effect for Scuttlebutt Ghoul (REV_900).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If you control
a <b>Secret</b>, summon a
copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_900t")