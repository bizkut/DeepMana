"""Effect for Frenzied Fangs (CORE_REV_350).

Card Text: Summon two 2/1 Bats.
<b>Infuse (3):</b> Give them +1/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_350t")