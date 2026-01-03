"""EX1_610 - Explosive Trap: When your hero is attacked, deal 2 damage to all enemies."""

def on_attack(game, owner, secret, attacker=None, defender=None):
    """
    Triggered when an enemy attacks.
    Only triggers if the hero is being attacked.
    """
    if defender and defender == owner.hero:
        # Deal 2 damage to all enemies
        for minion in list(attacker.controller.board):
            game.deal_damage(minion, 2, secret)
        game.deal_damage(attacker.controller.hero, 2, secret)
        return True
    return False

def on_play(game, player, card, target=None):
    """When the secret is played, add it to the secrets zone."""
    player.secrets.append(card)
