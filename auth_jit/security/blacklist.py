# A storage engine to save revoked tokens. in production,
# you can use Redis for storage system
class TokenBlacklist:
    def __init__(self):
        self._invalid_tokens = set()

    def invalidate_token(self, token):
        self._invalid_tokens.add(token)

    def is_token_invalid(self, token):
        return token in self._invalid_tokens
    
backList = TokenBlacklist()