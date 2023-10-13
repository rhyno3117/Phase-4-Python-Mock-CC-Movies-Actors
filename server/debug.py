#!/usr/bin/env python3
from faker import Faker

# from app import app
# from models import db, Movie, Actor, Credit

from faker.providers import lorem

fake = Faker()

fake.add_provider(lorem)




if __name__ == '__main__':
    print(fake.paragraph(nb_sentences=2))