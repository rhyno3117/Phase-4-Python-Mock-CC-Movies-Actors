#!/usr/bin/env python3
from faker import Faker

# from app import app
# from models import db, Movie, Actor, Credit

from faker.providers import internet

fake = Faker()

fake.add_provider(internet)




if __name__ == '__main__':
    print(fake.ipv4_private())