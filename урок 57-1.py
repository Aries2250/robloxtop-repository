import random

hair = ["brown", "black", "blonde", "red", "gray"]
eyes = ["blue", "green", "brown", "gray", "hazel"]
height = ["short", "average", "tall"]
build = ["slim", "average", "athletic", "heavy"]
features = ["freckles", "glasses", "beard", "tattoo", "piercing"]

def random_create_character():
    character = {
        "hair": random.choice(hair),
        "eyes": random.choice(eyes),
        "height": random.choice(height),
        "build": random.choice(build),
        "features": random.sample(features, k=random.randint(0, 2))  # Up to 2 random features
    }
    return character

print(random_create_character())
