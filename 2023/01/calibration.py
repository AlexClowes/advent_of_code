def main():
    with open("calibration_doc.txt") as f:
        total = 0
        for line in f:
            digits = [char for char in line if char.isdigit()]
            total += int(digits[0] + digits[-1])
        print(total)




if __name__ == "__main__":
    main()
