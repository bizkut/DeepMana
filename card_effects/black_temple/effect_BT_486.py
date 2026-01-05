"""Effect for Pit Commander (BT_486).

Card Text: <b>Taunt</b>
At the end of your turn, summon a Demon from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_486t")