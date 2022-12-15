def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


def parse_input(data) -> list:
    sensor_list = []
    for datapoints in data:
        line = datapoints.strip()
        _, _, sx, sy, _, _, _, _, bx, by = line.split()
        sx, sy, bx, by = int(sx[2:-1]), int(sy[2:-1]), int(bx[2:-1]), int(by[2:])
        coordinate_tuple = (sx, sy, bx, by)
        sensor_list.append(coordinate_tuple)
    return sensor_list


def part_one(beacon_tuples, row_nr) -> int:
    beacons = set()
    sensors = []
    minimum_x = minimum_y = 10**10
    maximum_x = maximum_y = 0
    for sx, sy, bx, by in beacon_tuples:
        beacons.add((bx, by))
        radius = abs(sx-bx) + abs(sy-by)
        sensors.append((sx, sy, radius))
        if sx - radius < minimum_x:
            minimum_x = sx - radius
        if sx + radius > maximum_x:
            maximum_x = sx + radius
        if sy - radius < minimum_y:
            minimum_y = sx - radius
        if sy + radius > maximum_y:
            maximum_y = sy + radius

    nr_of_no_beacons = 0
    for x_pointer in range(minimum_x, maximum_y + 1):
        # skip potential beacons we know of, obviously (>ლ)
        if (x_pointer, row_nr) in beacons:
            continue
        # check if pointer is in the radius of any relevant sensor
        for sx, sy, radius in sensors:
            # is it a relevant sensor?
            if (sy <= row_nr <= sy + radius) or (sy >= row_nr >= sy - row_nr):
                distance = abs(x_pointer - sx) + abs(row_nr - sy)
                if distance <= radius:
                    nr_of_no_beacons += 1
                    break
    return nr_of_no_beacons


if __name__ == '__main__':
    print(f"Answer 1 for day 15 is {part_one(parse_input(read_input_for_testing('inputs/input_15.txt')), 2000000)}")
    # print(f"Answer 2 for day 15 is {part_two(parse_input(read_input_for_testing('inputs/input_15.txt')))}")
