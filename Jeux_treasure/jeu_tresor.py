def create_map(size, trapsNbr):
    co_map = {}
    co_tresor = (random.randint(1, size), random.randint(1, size))
    co_map[co_tresor] = 1
    for _ in range(trapsNbr):
        coord = (random.randint(1, size), random.randint(1, size))
        while coord in co_map:
            coord = (random.randint(1, size), random.randint(1, size))
        co_map[coord] = -1
    return co_map


def demander_coord(map_size):
    ligne = input().strip()
    parts = ligne.split()
    if len(parts) != 2:
        return None
    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        return None
    if 1 <= x <= map_size and 1 <= y <= map_size:
        return (x, y)
    return None


def play_game(map_size, treasure_map):
    while True:
        coord = demander_coord(map_size)
        if coord is not None and coord in treasure_map:
            return treasure_map[coord] == 1




