def main():
    with open("timetable.txt") as f:
        start_time = int(f.readline().strip())
        bus_ids = [int(id) for id in f.readline().strip().split(",") if id != "x"]

    delay_id = min((id - start_time % id, id) for id in bus_ids)
    print(delay_id[0] * delay_id[1])


if __name__ == "__main__":
    main()
