"""Effect for Curse of Agony (ONY_034).

Card Text: [x]Shuffle three Agonies
into the opponent's deck.
They deal Fatigue damage
when drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)