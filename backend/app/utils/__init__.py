import random


def generate_token(length):
    chars = (
        "abcdefghijklmnopqrstuvwxyz" "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "0123456789"
    )

    rand = random.SystemRandom()
    return "".join(rand.choice(chars) for x in range(length))
