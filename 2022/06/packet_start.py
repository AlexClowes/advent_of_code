def get_packet_start_pos(stream, window_size):
    for count in range(window_size, len(stream)):
        if len(set(stream[count - window_size : count])) == window_size:
            return count


def main():
    with open("datastream.txt") as f:
        stream = f.read().strip()

    print(get_packet_start_pos(stream, 4))
    print(get_packet_start_pos(stream, 14))



if __name__ == "__main__":
    main()
