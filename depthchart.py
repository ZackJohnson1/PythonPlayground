import json
import os


class DepthChart:
    def __init__(self, file_path='depth_chart.json'):
        self.file_path = file_path
        self.depth_chart = {
            'QB': [],
            'RB': [],
            'WR': [],
            'TE': [],
            'LT': [],
            'LG': [],
            'C': [],
            'RG': [],
            'RT': [],
            'DE': [],
            'DT': [],
            'LB': [],
            'CB': [],
            'S': [],
            'K': [],
            'P': [],
            'KR': [],
            'PR': []
        }
        self.position_map = {
            'QB': ['qb', 'quarterback'],
            'RB': ['rb', 'running back'],
            'WR': ['wr', 'wide receiver'],
            'TE': ['te', 'tight end'],
            'LT': ['lt', 'left tackle'],
            'LG': ['lg', 'left guard'],
            'C': ['c', 'center'],
            'RG': ['rg', 'right guard'],
            'RT': ['rt', 'right tackle'],
            'DE': ['de', 'defensive end'],
            'DT': ['dt', 'defensive tackle'],
            'LB': ['lb', 'linebacker'],
            'CB': ['cb', 'cornerback'],
            'S': ['s', 'safety'],
            'K': ['k', 'kicker'],
            'P': ['p', 'punter'],
            'KR': ['kr', 'kick returner'],
            'PR': ['pr', 'punt returner']
        }
        self.load_depth_chart()

    def normalize_position(self, position):
        position = position.strip().lower()
        for key, aliases in self.position_map.items():
            if position in aliases:
                return key
        return None

    def save_depth_chart(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.depth_chart, file)
        print("Depth chart saved successfully.")

    def load_depth_chart(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.depth_chart = json.load(file)
            print("Depth chart loaded successfully.")
        else:
            print("No saved depth chart found. Starting with an empty chart.")

    def add_player(self, position, player_name):
        normalized_position = self.normalize_position(position)
        if not normalized_position:
            print(f"Position '{position}' not recognized. Please choose a valid position.")
            return

        if len(self.depth_chart[normalized_position]) < 4:
            self.depth_chart[normalized_position].append(player_name)
            print(
                f"Added {player_name} as the {len(self.depth_chart[normalized_position])}th string {normalized_position}.")
            self.save_depth_chart()
        else:
            print(f"The depth chart for {normalized_position} is already full (1st to 4th string).")

    def move_player(self, current_position, player_name, new_position):
        normalized_current = self.normalize_position(current_position)
        normalized_new = self.normalize_position(new_position)

        if not normalized_current or not normalized_new:
            print("One or both positions are not recognized. Please choose valid positions.")
            return

        if player_name not in self.depth_chart[normalized_current]:
            print(f"{player_name} is not listed in the {current_position} depth chart.")
            return

        # Remove the player from the current position
        self.depth_chart[normalized_current].remove(player_name)
        print(f"Removed {player_name} from {normalized_current}.")

        # Ask for the string position in the new position
        while True:
            try:
                string_position = int(input(f"Enter the string position (1-4) for {player_name} in {new_position}: "))
                if 1 <= string_position <= 4:
                    if len(self.depth_chart[normalized_new]) >= string_position:
                        self.depth_chart[normalized_new].insert(string_position - 1, player_name)
                    else:
                        self.depth_chart[normalized_new].append(player_name)
                    print(f"Added {player_name} as the {string_position}th string {normalized_new}.")
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        self.save_depth_chart()

    def display_depth_chart(self):
        print("\n--- Football Depth Chart ---")
        for position, players in self.depth_chart.items():
            full_position_name = next((name for name, aliases in self.position_map.items() if name == position),
                                      position)
            print(f"\n{full_position_name}:")
            if players:
                for i, player in enumerate(players, start=1):
                    print(f"  {i}th String: {player}")
            else:
                print("  No players assigned.")

    def display_starting_11(self):
        print("\n--- Starting 11 ---")

        # Offense
        offense_positions = [
            ('QB', 1), ('RB', 1), ('TE', 1), ('LT', 1), ('RT', 1),
            ('LG', 1), ('RG', 1), ('C', 1), ('WR', 3)
        ]
        print("\nOffense:")
        for pos, count in offense_positions:
            for i in range(count):
                player = self.depth_chart[pos][i] if i < len(self.depth_chart[pos]) else "[Position not filled]"
                print(f"  {pos}: {player}")

        # Defense
        defense_positions = [
            ('DE', 2), ('DT', 2), ('LB', 3), ('S', 2), ('CB', 2)
        ]
        print("\nDefense:")
        for pos, count in defense_positions:
            for i in range(count):
                player = self.depth_chart[pos][i] if i < len(self.depth_chart[pos]) else "[Position not filled]"
                print(f"  {pos}: {player}")


def menu():
    depth_chart = DepthChart()
    while True:
        print("\nFootball Depth Chart Manager")
        print("1. Add Player")
        print("2. Move Player")
        print("3. View Depth Chart")
        print("4. View Starting 11")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            position = input("Enter the position: ")
            player_name = input("Enter the player's name: ")
            depth_chart.add_player(position, player_name)

        elif choice == '2':
            current_position = input("Enter the current position of the player: ")
            player_name = input("Enter the player's name: ")
            new_position = input("Enter the new position for the player: ")
            depth_chart.move_player(current_position, player_name, new_position)

        elif choice == '3':
            depth_chart.display_depth_chart()

        elif choice == '4':
            depth_chart.display_starting_11()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    menu()