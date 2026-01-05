"""Effect for Double Agent (AV_711).

Card Text: [x]<b>Battlecry:</b> If you're holding
a card from another class,
 summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_711t")