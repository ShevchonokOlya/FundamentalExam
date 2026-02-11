def add_stop(start_index: int, substring: str, line: str) -> str:
    if start_index < len(line):
        line_before = line[:start_index]
        line_after = line[start_index:]
        line = line_before + substring + line_after
        return line
    return line


def remove_stop(start_index: int, end_index: int, line: str) -> str:
    if 0 <= start_index <= end_index < len(line):
        line_before = line[:start_index]
        line_after = line[end_index + 1:]
        return line_before + line_after
    return line


def switch(old_string: str, new_string: str, line: str) -> str:
    line = line.replace(old_string, new_string)
    return line


def word_tour():
    travel_line = input()
    while True:
        command = input().split(":")
        if command[0] == "Travel":
            break
        elif command[0] == "Add Stop":
            travel_line = add_stop(int(command[1]), command[2], travel_line)
            print(travel_line)
        elif command[0] == "Remove Stop":
            travel_line = remove_stop(int(command[1]), int(command[2]), travel_line)
            print(travel_line)
        elif command[0] == "Switch":
            travel_line = switch(command[1], command[2], travel_line)
            print(travel_line)

    print(f"Ready for world tour! Planned stops: {travel_line}")


def activation_keys():
    activation_line = input()
    while True:
        command = input().split(">>>")
        if command[0] == "Generate":
            break
        if command[0] == "Contains":
            substring = command[1]
            if substring in activation_line:
                print(f"{activation_line} contains {substring}")
            else:
                print(f"Substring not found!")

        if command[0] == "Flip":
            upper_lower = command[1]
            start_index = int(command[2])
            end_index = int(command[3])

            if 0 <= start_index < end_index < len(activation_line):
                line_before = activation_line[:start_index]
                line_after = activation_line[end_index:]
                substring = activation_line[start_index: end_index]
                if upper_lower == "Upper":
                    substring = substring.upper()
                else:
                    substring = substring.lower()

                activation_line = line_before + substring + line_after
                print(activation_line)

        if command[0] == "Slice":
            start_index = int(command[1])
            end_index = int(command[2])

            if 0 <= start_index < end_index < len(activation_line):
                line_before = activation_line[:start_index]
                line_after = activation_line[end_index:]
                activation_line = line_before + line_after
            print(activation_line)

    print(f"Your activation key is: {activation_line}")


def mirror_word():
    import re
    mirror_words = []

    input_line = input()
    pattern = r"([#@])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1{1}"

    matches = re.findall(pattern, input_line)
    for match in matches:
        if match[1] == match[2][::-1]:
            mirror_words.append(f"{match[1]} <=> {match[2]}")

    if not matches:
        print("No word pairs found!")
    else:
        print(f"{len(matches)} word pairs found!")

    if mirror_words:
        print("The mirror words are:")
        print(", ".join(mirror_words))
    else:
        print("No mirror words!")


def destination_mapper():
    import re
    input_line = input()
    pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"
    matches = re.findall(pattern, input_line)
    destinations = []
    travel_points = 0

    for match in matches:
        destinations.append(match[1])
        travel_points += len(match[1])

    print("Destinations:", ", ".join(destinations))
    print(f"Travel Points: {travel_points}")


def plant_discovery():
    n = int(input())

    plants_rarity = {}
    plants_rating = {}
    for _ in range(n):
        plant_input = input().split("<->")
        plants_name = plant_input[0]
        rarity = int(plant_input[1])
        plants_rarity[plants_name] = rarity
        plants_rating[plants_name] = []

    while True:
        command = input()
        if command == "Exhibition":
            break

        option = command.split(": ")
        if option[0] == "Rate":
            plant = option[1].split(" - ")
            plant_name = plant[0]
            rating = float(plant[1])

            if plant_name in plants_rarity:
                plants_rating[plant_name].append(rating)
            else:
                print("error")

        elif option[0] == "Update":
            plant = option[1].split(" - ")
            plant_name = plant[0]
            rarity = int(plant[1])

            if plant_name in plants_rarity:
                plants_rarity[plant_name] = rarity
            else:
                print("error")

        elif option[0] == "Reset":
            plant_name = option[1]

            if plant_name in plants_rarity:
                plants_rating[plant_name].clear()
            else:
                print("error")

    print("Plants for the exhibition:")
    for plant_name, rarity in plants_rarity.items():
        average_rating = 0.00
        if len(plants_rating[plant_name]) > 0:
            average_rating = sum(plants_rating[plant_name]) / len(plants_rating[plant_name])

        print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")


HERO_NAME = str
HERO_HP = int
HERO_MP = int
Hero_parameters = [HERO_HP, HERO_MP]
Hero_dict = {HERO_NAME: Hero_parameters}


def heroes_of_code_and_logic():
    max_hp = 100
    max_mp = 200
    heroes_dict: Hero_dict = {}

    number_of_heroes = int(input())
    for _ in range(number_of_heroes):
        heroes = input().split()
        hero_name = heroes[0]
        hit_points = int(heroes[1])
        mana_points = int(heroes[2])
        heroes_dict[hero_name] = [hit_points, mana_points]

    while True:
        command = input().split(" - ")
        if command[0] == "End":
            break
        if command[0] == "CastSpell":
            hero_name = command[1]
            mp_needed = int(command[2])
            spell_name = command[3]
            heroes_mp = heroes_dict[hero_name][1]

            if heroes_mp >= mp_needed:
                res_mp = heroes_mp - mp_needed
                heroes_dict[hero_name][1] = res_mp
                print(f"{hero_name} has successfully cast {spell_name} and now has {res_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        if command[0] == "TakeDamage":
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            current_hp = heroes_dict[hero_name][0] - damage

            if current_hp > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
                heroes_dict[hero_name][0] = current_hp
            else:
                heroes_dict.pop(hero_name)
                print(f"{hero_name} has been killed by {attacker}!")

        if command[0] == "Recharge":
            hero_name = command[1]
            mp_points = int(command[2])
            recovery_mp_points = min(max_mp - heroes_dict[hero_name][1], mp_points)
            heroes_dict[hero_name][1] = heroes_dict[hero_name][1] + recovery_mp_points

            print(f"{hero_name} recharged for {recovery_mp_points} MP!")

        if command[0] == "Heal":
            hero_name = command[1]
            healing_points = int(command[2])
            recovery_points = min(max_hp - heroes_dict[hero_name][0], healing_points)

            heroes_dict[hero_name][0] = heroes_dict[hero_name][0] + recovery_points
            print(f"{hero_name} healed for {recovery_points} HP!")

    for hero_name, hero_attributes in heroes_dict.items():
        print(hero_name)
        print(f"  HP: {hero_attributes[0]}\n  MP: {hero_attributes[1]}")


def password_reset():
    password = input()

    while True:
        command_line = input()
        if command_line == "Done":
            break

        command = command_line.split()
        if command[0] == "TakeOdd":
            new_pass = [character for index, character in enumerate(password) if index % 2 == 1]
            password = "".join(new_pass)
            print(password)

        elif command[0] == "Cut":
            index = int(command[1])
            length = int(command[2])
            password = password[:index] + password[index + length:]
            print(password)

        elif command[0] == "Substitute":
            substring = command[1]
            substitute = command[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print("Nothing to replace!")

    print(f"Your password is: {password}")


def fancy_barcodes():
    import re
    n = int(input())
    for _ in range(n):
        barcode = input()
        pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
        matches = re.findall(pattern, barcode)
        if matches:
            products = {}
            for match in matches:
                products[match] = products.get(match, "00")
                digit_pattern = r'([\d]+)'
                digits = re.findall(digit_pattern, match)
                if digits:
                    products[match] = str("".join(digits))
                print(f"Product group: {products[match]}")
        else:
            print("Invalid barcode")


def secret_chat():
    concealed_message = input()
    while True:
        instructions = input()
        if instructions == "Reveal":
            break
        command = instructions.split(":|:")
        if command[0] == "InsertSpace":
            index = int(command[1])
            if 0 <= index < len(concealed_message):
                concealed_message = concealed_message[:index] + " " + concealed_message[index:]
            print(concealed_message)

        if command[0] == "Reverse":
            substring = command[1]
            if substring in concealed_message:
                concealed_message = concealed_message.replace(substring, "", 1)
                substring = substring[::-1]
                concealed_message = concealed_message + substring
                print(concealed_message)
            else:
                print("error")

        if command[0] == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            if substring in concealed_message:
                concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)

    print(f"You have a new text message: {concealed_message}")


def need_for_speed():
    number_of_cars = int(input())
    car_park = {}
    max_tank_volume = 75
    min_kilometers = 10_000
    max_kilometers = 100_000
    for _ in range(number_of_cars):
        car = input().split("|")
        car_name = car[0]
        mileage = int(car[1])
        fuel = int(car[2])
        car_park[car_name] = [mileage, fuel]

    while True:
        commands = input().split(" : ")
        command = commands[0]

        if command == "Stop":
            break

        car_name = commands[1]
        if command == "Drive":
            distance = int(commands[2])
            fuel = int(commands[3])

            fuel_available = car_park[car_name][1]

            if fuel <= fuel_available:
                car_park[car_name][0] += distance
                car_park[car_name][1] -= fuel
                print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

                if car_park[car_name][0] >= max_kilometers:
                    print(f"Time to sell the {car_name}!")
                    del car_park[car_name]

            else:
                print("Not enough fuel to make that ride")

        elif command == "Refuel":
            fuel = int(commands[2])
            recharged_fuel = min(max_tank_volume - car_park[car_name][1], fuel)
            car_park[car_name][1] += recharged_fuel
            print(f"{car_name} refueled with {recharged_fuel} liters")

        elif command == "Revert":
            kilometers = int(commands[2])
            current_kilometer = car_park[car_name][0]
            new_kilometer = current_kilometer - kilometers
            changed_kilometer = max(new_kilometer, min_kilometers)
            car_park[car_name][0] = changed_kilometer

            if new_kilometer >= min_kilometers:
                print(f"{car_name} mileage decreased by {kilometers} kilometers")

    for car, parameters in car_park.items():
        print(f"{car} -> Mileage: {parameters[0]} kms, Fuel in the tank: {parameters[1]} lt.")


def the_pianist():
    number_of_pieces = int(input())
    music_collection = {}

    for _ in range(number_of_pieces):
        pieces = input().split("|")
        piece_calling_like = pieces[0]
        composer = (pieces[1])
        key = (pieces[2])
        music_collection[piece_calling_like] = [composer, key]

    while True:
        commands = input().split("|")
        command = commands[0]

        if command == "Stop":
            break

        piece_name = commands[1]
        if command == "Add":
            composer = commands[2]
            key = commands[3]
            if piece_name not in music_collection.keys():
                music_collection[piece_name] = [composer, key]
                print(f"{piece_name} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece_name} is already in the collection!")

        elif command == "Remove":
            if piece_name in music_collection.keys():
                del music_collection[piece_name]
                print(f"Successfully removed {piece_name}!")
            else:
                print(f"Invalid operation! {piece_name} does not exist in the collection.")

        elif command == "ChangeKey":
            new_key = commands[2]
            if piece_name in music_collection.keys():
                music_collection[piece_name][1] = new_key
                print(f"Changed the key of {piece_name} to {new_key}!")
            else:
                print(f"Invalid operation! {piece_name} does not exist in the collection.")

    for piece, piece_description in music_collection.items():
        print(f"{piece} -> Composer: {piece_description[0]}, Key: {piece_description[1]}")


def the_imitation_game():
    encrypted_message = input()
    while True:
        instructions = input().split("|")
        if instructions[0] == "Decode":
            break

        if instructions[0] == "Move":
            number_of_letters = int(instructions[1])
            encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

        elif instructions[0] == "Insert":
            index = int(instructions[1])
            value = instructions[2]
            encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

        elif instructions[0] == "ChangeAll":
            substring = instructions[1]
            replacement = instructions[2]
            encrypted_message = encrypted_message.replace(substring, replacement)
    print(f"The decrypted message is: {encrypted_message}")


class Food:
    def __init__(self, food_name: str, expire_date: str, calories: str):
        self.name = food_name
        self.expire_date = expire_date
        self.calories = int(calories)


def ad_astra():
    import re
    total_food = []

    calories_per_day = 2000

    text_string = input()
    pattern = r"([#|])(([A-Z][a-z]+[ ]*)+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

    matches = re.findall(pattern, text_string)
    for match in matches:
        food_name = match[1]
        date = match[3]
        calories = match[4]
        food = Food(food_name, date, calories)
        total_food.append(food)

    summarize_calories = sum([food.calories for food in total_food])
    days = summarize_calories // calories_per_day
    print(f"You have food to last you for: {days} days!")
    for food in total_food:
        print(f"Item: {food.name}, Best before: {food.expire_date}, Nutrition: {food.calories}")


def multiply_my_list(list_of_numbers: list[int]):
    res = 1
    for number in list_of_numbers:
        res *= number
    return res


def ascii_from_the_word(emoji_string: str):
    sum_char = 0
    for char in emoji_string:
        sum_char += ord(char)
    return sum_char


def emoji_detector():
    import re
    import math

    sentence = input()

    cool_threshold_pattern = r"\d"
    matches = re.findall(cool_threshold_pattern, sentence)
    multiplying_number = math.prod(map(int, matches))
    print(f"Cool threshold: {multiplying_number}")

    smile_pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

    emoji_matches = re.findall(smile_pattern, sentence)

    print(f"{len(emoji_matches)} emojis found in the text. The cool ones are:")

    for match in emoji_matches:
        separator = match[0]
        name = match[1]

        coolness = ascii_from_the_word(name)

        if coolness >= multiplying_number:
            full_emoji = separator + name + separator
            print(full_emoji)


def pirates():
    attack_geography = {}
    while True:
        instructions = input()
        if instructions == "Sail":
            break
        city, population, gold = [int(x) if x.isdigit() else x for x in instructions.split("||")]
        if city not in attack_geography:
            attack_geography[city] = [population, gold]
        else:
            attack_geography[city][0] += population
            attack_geography[city][1] += gold

    while True:
        events = input()
        if events == "End":
            break

        # Plunder=>{town}=>{people}=>{gold} "Prosper=>{town}=>{gold}"

        command = events.split("=>")
        if command[0] == "Plunder":
            town = command[1]
            people = int(command[2])
            gold = int(command[3])

            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            attack_geography[town][0] -= people
            attack_geography[town][1] -= gold

            if min(attack_geography[town]) <= 0:
                del attack_geography[town]
                print(f"{town} has been wiped off the map!")


        elif command[0] == "Prosper":
            town = command[1]
            gold = int(command[2])
            if gold < 0:
                print("Gold added cannot be a negative number!")
                continue

            attack_geography[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {attack_geography[town][1]} gold.")


    if attack_geography:
        print(f"Ahoy, Captain! There are {len(attack_geography)} wealthy settlements to go to:")
        for town, [people, gold] in attack_geography.items():
            print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
    else:
        print(f"Ahoy, Captain! All targets have been plundered and destroyed!")



pirates()
