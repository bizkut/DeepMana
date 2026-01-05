"""Effect for Spinel Spellstone (TOY_825t).

Card Text: Give Undead in your hand +2/+2. <i>(Gain 5 <b>Corpses</b> to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
