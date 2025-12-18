

def get_travel_path(ancestor, date):
    if date <= 1440:
        return [(ancestor, date)]
    if ancestor not in ASCENDANCE:
        return []
    for anc, date_anc in ASCENDANCE[ancestor]:
        if date - date_anc < 0 or date - date_anc > 100:
            continue
        suite = get_travel_path(anc, date_anc)
        if suite != []:
            return[(ancestor, date)] + suite
    return []



ASCENDANCE = {
        "Rita": [("Paule", 1927),("Sacha", 1928)],
        "Sacha": [("Renee", 1839), ("Claude", 1837)],
        "Paule": [("Francoise", 1440), ("Antoine", 1841)],
        "Renee": [("Emmanuel", 1755), ("Charlotte", 1753)],
        "Emmanuel": [("Marguerite", 1666), ("Hugues", 1664)],
        "Marguerite": [("Pedro", 1569), ("Sofia", 1571)],
        "Pedro": [("Mercedes", 1498), ("Luis", 1500)],
        "Mercedes": [("Isabella", 1438), ("Juan", 1427)],
        "Isabella": [("Jose", 1376), ("Maria", 1378)]
        }

print(get_travel_path("Rita", 2025))

        
