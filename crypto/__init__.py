from passlib.hash import argon2
import secrets


class Service:
    @staticmethod
    def hash_password(password):
        return argon2.using(rounds=5).hash(password)

    @staticmethod
    def verify_password(password, hash):
        return argon2.verify(password, hash)

    @staticmethod
    def generate_dummytoken():
        return secrets.token_urlsafe(16)
