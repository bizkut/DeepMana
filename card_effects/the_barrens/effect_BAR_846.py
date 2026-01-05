"""Effect for Mor'shan Elite (BAR_846).

Card Text: [x]<b>Taunt</b>. <b>Battlecry:</b> If your hero
attacked this turn, summon
a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_846t")