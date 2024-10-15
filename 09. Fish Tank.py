def fish_tank(length, width, height, percent):
    tank_volume = (length * width * height) / 1000
    total_water = tank_volume - (tank_volume * (percent / 100))

    return total_water


l = int(input())
w = int(input())
h = int(input())
perc = float(input())
print(fish_tank(l, w, h, perc))
