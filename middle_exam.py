def journey_to_artifact():
    initial_energy = float(input())  # 10.0 - 150.0.
    mountain_count = 0

    while True:
        terrains = input()
        if terrains == "Journey ends here!":
            if mountain_count < 9:
                we_have_artefacts = mountain_count // 3
                we_need_more = 3 - we_have_artefacts
                print(
                    f"The character could not find all the pieces and needs {we_need_more} more to complete the legendary artifact.")
            break

        if terrains == "mountain":
            initial_energy -= 10

            if initial_energy >= 0:
                mountain_count += 1

            if mountain_count >= 9:
                print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
                return

        elif terrains == "desert":
            initial_energy -= 15

        elif terrains == "forest":
            initial_energy += 7

        if initial_energy <= 0:
            print(f"The character is too exhausted to carry on with the journey.")
            break


def robots_adventure():
    city_items = list(map(int, input().split("|")))
    total_items = 0

    while True:
        command = input()

        if command == "Adventure over":
            break

        commands = command.split(" ")
        if commands[0] == "Step":
            what_step = commands[1].split("$")  # ['Backward', '0', '12']
            start_index = int(what_step[1])
            steps = int(what_step[2]) % len(city_items)
            if 0 <= start_index < len(city_items):
                if what_step[0] == "Backward":

                    index = (start_index - steps) % len(city_items)
                    total_items += city_items[index]
                    city_items[index] = 0

                elif what_step[0] == "Forward":
                    index = (start_index + steps) % len(city_items)

                    total_items += city_items[index]
                    city_items[index] = 0

        elif commands[0] == "Double":
            index = int(commands[1])
            if 0 <= index < len(city_items):
                city_items[index] *= 2

        elif commands[0] == "Switch":
            city_items = city_items[::-1]

    print(" - ".join(map(str, city_items)))
    print(f"Robo finished the adventure with {total_items} items!")


def music_playlist():

    list_of_songs = input().split()
    n = int(input())

    for _ in range(n):
        command = input().split(" * ")
        if command[0] == "Add Song":
            name_of_song = command[1]
            if name_of_song not in list_of_songs:
                list_of_songs.append(name_of_song)
                print(f"{name_of_song} successfully added")

        elif command[0] == "Delete Song":
            number_of_songs = int(command[1])
            if len(list_of_songs) >= number_of_songs:
                print(", ".join(list_of_songs[:number_of_songs]), "deleted")
                list_of_songs = list_of_songs[number_of_songs:]

        elif command[0] == "Shuffle Songs":
            firs_index = int(command[1])
            second_index = int(command[2])
            if 0 <= firs_index < len(list_of_songs) and 0 <= second_index < len(list_of_songs):
                list_of_songs[firs_index], list_of_songs[second_index] = list_of_songs[second_index], list_of_songs[firs_index]
                print(f"{list_of_songs[firs_index]} is swapped with {list_of_songs[second_index]}")

        elif command[0] == "Insert":
            song_name = command[1]
            index_to_insert = int(command[2])

            if 0 <= index_to_insert < len(list_of_songs):
                if song_name not in list_of_songs:
                    list_of_songs = list_of_songs[: index_to_insert] + [song_name] + list_of_songs[index_to_insert:]
                    print(f"{song_name} successfully inserted")
                else:
                    print("Song is already in the playlist")
            else:
                print("Index out of range")

        elif command[0] == "Sort":
            list_of_songs.sort(reverse=True)

        elif command[0] == "Play":
            break

    print("Songs to Play:")
    print("\n".join(list_of_songs))

def moving_targets():

    targets = [int(t) for t in input().split()]

    while True:
        command_line = input()
        if command_line == "End":
            break
        else:
            command, second_parameter, third_parameter = command_line.split()
            index = int(second_parameter)


            if command == "Shoot":
                power = int(third_parameter)
                if index in range(0, len(targets)):
                    targets[index] -= power
                    if targets[index] <= 0:
                        targets.pop(index)


            elif command == "Add":
                value = int(third_parameter)
                if index in range(0, len(targets)):
                    targets.insert(index, value)
                else:
                    print("Invalid placement!")
                pass

            elif command == "Strike":
                shift = int(third_parameter)
                if index in range(0, len(targets)) and index + shift < len(targets) and  index - shift >= 0:
                    targets = targets[:index - shift] + targets[index + shift + 1:]
                else:
                    print("Strike missed!")


    print("|".join(map(str, targets)))

moving_targets()