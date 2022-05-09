# 7 kyu
# Thinkful - Logic Drills: Umbrella decider


def take_umbrella(weather, rain_chance):
    if weather in ['rainy', 'cloudy'] and rain_chance > 0.20:
        return True
    return False



print(take_umbrella('sunny', 0.40), False)
print(take_umbrella('rainy', 0.0), True)
print(take_umbrella('cloudy', 0.20), False)
