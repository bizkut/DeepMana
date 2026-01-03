"""EX1_554 - Snipe: When your opponent plays a minion, deal 4 damage to it."""

def on_minion_played(game, owner, secret, minion=None):
    """
    Triggered when opponent plays a minion.
    Deal 4 damage to that minion.
    """
    if minion:
        game.deal_damage(minion, 4, secret)
        return True
    return False

def on_play(game, player, card, target=None):
    """When the secret is played, add it to the secrets zone."""
    player.secrets.append(card)
