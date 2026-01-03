"""EX1_294 - Mirror Entity: When your opponent plays a minion, summon a copy of it."""

def on_minion_played(game, owner, secret, minion=None):
    """
    Triggered when opponent plays a minion.
    Summon a copy of that minion for the secret owner.
    """
    if minion and len(owner.board) < 7:
        from simulator.factory import create_card
        from simulator.entities import Minion
        
        # Create a copy of the minion
        copy = create_card(minion.card_id, game)
        if copy:
            minion_copy = Minion(copy.data, game) if not isinstance(copy, Minion) else copy
            minion_copy.controller = owner
            owner.summon(minion_copy)
        return True
    return False

def on_play(game, player, card, target=None):
    """When the secret is played, add it to the secrets zone."""
    player.secrets.append(card)
