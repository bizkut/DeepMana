"""Effect for Mindrender Illucia (SCH_159).

Card Text: [x]<b>Battlecry:</b> Replace
your hand with a copy of
your opponent's until
end of turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass