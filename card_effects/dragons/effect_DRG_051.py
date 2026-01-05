"""Effect for Strength in Numbers (DRG_051).

Card Text: <b>Sidequest:</b> Spend 10 Mana on minions.
<b>Reward:</b> Summon a minion from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_051t")