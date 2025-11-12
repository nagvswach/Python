def belongs_to_file(word, filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            mot = line.strip()
            if mot == word:
                return True
    return False


