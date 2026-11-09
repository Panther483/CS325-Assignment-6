def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()
    dogs_fed = 0
    m = 0
    n = 0
    while m < len(hunger_level) and n < len(biscuit_size):
        if hunger_level[m] <= biscuit_size[n]:
            dogs_fed += 1
            m += 1
            n += 1
        else:
            n += 1
    return dogs_fed