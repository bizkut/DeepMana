"""Effect for Ruinous Velocidrake (TIME_029).

Card Text: [x]<b>Rush</b>
<b>Battlecry:</b> Cast a Shred
 of Time from your deck to
   summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_029t")