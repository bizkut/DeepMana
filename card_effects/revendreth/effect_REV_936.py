"""Effect for Crud Caretaker (REV_936).

Card Text: <b>Battlecry</b>: Summon a 3/5 Elemental with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_936t")