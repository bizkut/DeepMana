"""Effect for Steel Beetle (YOD_040).

Card Text: <b>Battlecry:</b> If you're holding a spell that costs (5) or more, gain 5 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(5)