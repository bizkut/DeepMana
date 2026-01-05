"""Effect for Coilskar Commander (TSC_609).

Card Text: [x]<b>Taunt</b>. <b>Battlecry:</b> If you've
cast three spells while
holding this, summon two
  copies of this.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_609t")