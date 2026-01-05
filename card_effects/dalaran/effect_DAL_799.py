"""Effect for Crystal Stag (DAL_799).

Card Text: <b>Rush</b>. <b>Battlecry:</b> If you've restored 5 Health this game, summon a copy of this.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_799t")