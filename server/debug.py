#!/usr/bin/env python3

from app import app
from models import db, Movie, Actor, Credit

if __name__ == '__main__':
    with app.app_context():
        pass