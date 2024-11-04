import random

fun_facts = [
    "The first computer virus was created in 1986 and was called Brain.",
    "The first 1GB hard drive was announced in 1980 and weighed over 500 pounds.",
    "More than 500 hours of video are uploaded to YouTube every minute.",
    "The first iPhone was released in 2007, revolutionizing smartphones.",
    "In 2023, there are more mobile devices on Earth than there are people.",
    "The first email ever sent was in 1971 by Ray Tomlinson.",
    "There are over 4.9 billion internet users worldwide as of 2021.",
    "The QWERTY keyboard layout was designed to slow down typing!",
    "The first video game was created in 1958 and was a simple tennis game.",
    "Did you know that 90% of the world's data has been created in the last two years?"
]

random_facts = random.choice(fun_facts)
print(f"Fun Fact About Tech: {random_facts}")
