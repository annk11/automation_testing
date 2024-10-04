import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class UserData:
    username = 'nikia'
    password = 'wer'


class DataGenerator:
    name = generate_random_string(10)
    description = generate_random_string(50)