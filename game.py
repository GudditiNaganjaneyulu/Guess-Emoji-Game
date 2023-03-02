import random
from time import time

class Room:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.players = [creator]
        self.words = []
        self.game_started = False

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def add_word(self, word):
        self.words.append(word)

    def start_game(self):
        if len(self.players) < 2:
            print("Cannot start game with less than 2 players")
            return
        if not self.words:
            print("Cannot start game without any words")
            return
        self.game_started = True
        teams = {
            "Team 1": [],
            "Team 2": []
        }
        for i, player in enumerate(self.players):
            team_name = "Team 1" if i % 2 == 0 else "Team 2"
            teams[team_name].append(player)
        print("Game started!")
        for word in self.words:
            print("New word:", word)
            correct_guess = False
            start_time = time()
            while time() - start_time < 60:
                guess = input("Guess the word: ")
                if guess.lower() == word.lower():
                    print("Correct!")
                    correct_guess = True
                    break
            if not correct_guess:
                print("Time's up!")
            for team, players in teams.items():
                if guesser in players:
                    score = players.count(guesser)
                    if correct_guess:
                        score += 1
                    print(f"{team}: {score} points")
        print("Game over!")

creator = input("Enter creator name: ")
room_name = input("Enter room name: ")
room = Room(room_name, creator)
while True:
    action = input("Enter action (add_player, remove_player, add_word, start_game, quit): ")
    if action == "add_player":
        player = input("Enter player name: ")
        room.add_player(player)
    elif action == "remove_player":
        player = input("Enter player name: ")
        room.remove_player(player)
    elif action == "add_word":
        word = input("Enter word: ")
        room.add_word(word)
    elif action == "start_game":
        room.start_game()
    elif action == "quit":
        break
    else:
        print("Invalid action")
