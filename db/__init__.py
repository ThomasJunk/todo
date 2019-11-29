"""Database module
"""
from tinydb import TinyDB


def create_database(filename):
    """Factory function to set up a tinydb database

    Args:
        filename (string): filename to store temporary .json
    Returns:
        TinyDB: instance of TinyDB
    """
    return TinyDB(filename)
