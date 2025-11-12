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

