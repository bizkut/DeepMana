"""Effect for Endangered Dodo (TIME_703).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If you have 10 or
less Health, gain +5/+5 and
   summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_703t")