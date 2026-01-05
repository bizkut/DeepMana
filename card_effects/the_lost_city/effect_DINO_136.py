"""Effect for Horn of Feasting (DINO_136).

Card Text: Summon three
2/1 Raptors with <b>Rush</b>.
<b>Outcast:</b> Give them <b>Immune</b>
while attacking this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_136t")