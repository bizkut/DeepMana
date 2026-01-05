"""Effect for Bronze Dragonknight (WON_052).

Card Text: [x]<b>Taunt</b>. <b>Battlecry:</b> If this
has 5 or more Attack,
 summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_052t")