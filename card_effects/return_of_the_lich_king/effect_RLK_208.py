"""Effect for Fel'dorei Warband (RLK_208).

Card Text: Deal $4 damage.
If your deck has no minions, summon four 1/1 Illidari with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)