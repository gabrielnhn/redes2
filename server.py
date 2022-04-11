import random

def get_temperature(weather):
    if weather == "hot":
        return random.randint(25, 35)
    else:
        return random.randint(-5, 10)

if __name__ == "__main__":

    if random.randint(0, 1):
        weather = "hot"
    else:
        weather = "cold"



