from random import randint

class Game:
    def __init__(self):
        self.round_to_win = 0
        self.quantity_round = 1
        self.score_bot = 0
        self.score_player = 0
        self.naming_dict = {1:'stone', 2:'scissors', 3:'paper', 4:'lizard', 5:'Spok'}

    def get_random_elements(self):
        random_choice = randint(1,5)
        return self.naming_dict.get(random_choice)

    @staticmethod
    def get_winner(player_choice, bot_choice):
        if player_choice == bot_choice:
            return 'Draw'
        elif (player_choice == 'scissors' and bot_choice == 'paper')or \
            (player_choice == 'scissors' and bot_choice == 'lizard')or \
            (player_choice == 'stone' and bot_choice == 'scissors')or \
            (player_choice == 'stone' and bot_choice == 'lizard')or \
            (player_choice == 'paper' and bot_choice == 'stone')or \
            (player_choice == 'paper' and bot_choice == 'Spok')or \
            (player_choice == 'lizard' and bot_choice == 'Spok')or \
            (player_choice == 'lizard' and bot_choice == 'paper')or \
            (player_choice == 'Spok' and bot_choice == 'scissors')or \
            (player_choice == 'Spok' and bot_choice == 'stone'):
            return 'Player'
        else:
            return 'Bot'

    def count_score(self,winner):
        if winner == 'Player':
            self.score_player += 1
        elif winner == 'Bot':
            self.score_bot += 1
        self.quantity_round += 1

    @staticmethod
    def player_input():
        player_input = input(f'Игра началась! Сделай свой ход 1 = stone, 2 = scissors, 3 = paper, 4 = lizard, 5 = Spok: ')
        return int(player_input)

    def check_win(self):
        if self.score_player == self.round_to_win:
            return 'Player win'
        elif self.score_bot == self.round_to_win:
            return 'Bot win'
        else:
            return None

    def number_of_rounds_input(self):
        self.round_to_win = int(input(f'Введите количество раундов до победы: '))

    def game_started(self):
        self.number_of_rounds_input()
        while self.score_player < self.round_to_win and self.score_bot < self.round_to_win:
            print(f'Для победы нужно набрать {self.round_to_win} очков')
            bot_element = self.get_random_elements()
            player_number = self.player_input()
            player_element = self.naming_dict[player_number]
            print(f'Игрок выбрал {player_element} Бот выбрал {bot_element}')
            winner = self.get_winner(player_element, bot_element)
            self.count_score(winner)
            print(f'Победил {winner} Начинается раунд № {self.quantity_round}')
            print(f'Текущий счёт: Игрок - {self.score_player}, БОТ - {self.score_bot}')

a = Game()
a.game_started()





