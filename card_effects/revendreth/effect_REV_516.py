"""Effect for Vengeful Visage (REV_516).

Card Text: [x]<b>Secret:</b> After an enemy
minion attacks your hero,
summon a copy of it to
attack the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_516t")