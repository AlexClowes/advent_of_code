def main():
    with open("replacements.txt") as f:
        lines = [line.strip() for line in f]
        replacements = [line.split(" => ") for line in lines[:-2]]
        molecule = lines[-1]

    new_molecules = set()
    for old, new in replacements:
        for i in range(len(molecule) - len(old) + 1):
            if molecule[i: i + len(old)] == old:
                new_molecules.add(molecule[:i] + new + molecule[i + len(old):])

    print(len(new_molecules))


if __name__ == "__main__":
    main()
