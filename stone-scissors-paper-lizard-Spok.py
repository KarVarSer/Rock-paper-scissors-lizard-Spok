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


        rules = {
            'stone': ['scissors', 'lizard'],
            'paper': ['stone', 'Spok'],
            'scissors': ['paper', 'lizard'],
            'lizard': ['Spok', 'paper'],
            'Spok': ['scissors', 'stone']
        }


        return 'Player' if bot_choice in rules.get(player_choice, []) else 'Bot'

    def count_score(self,winner):
        if winner == 'Player':
            self.score_player += 1
        elif winner == 'Bot':
            self.score_bot += 1
        self.quantity_round += 1

    @staticmethod
    def player_input():
        while True:
            try:
                player_input = int(input(f'Игра началась! Сделай свой ход 1 = stone, 2 = scissors, 3 = paper, 4 = lizard, 5 = Spok: '))
                if 1 <= player_input <= 5:
                    return int(player_input)
                print('Ошибка выбери число от 1 до 5.')
            except ValueError:
                print('Ошибка введи целое число.')

    def check_win(self):
        if self.score_player == self.round_to_win:
            return 'Player win'
        elif self.score_bot == self.round_to_win:
            return 'Bot win'
        else:
            return None

    def number_of_rounds_input(self):
        while True:
            try:
                self.round_to_win = int(input(f'Введите количество раундов до победы: '))
                if 1 <= self.round_to_win <= 20:
                    break
                print('Введите количество раундов до победы ')
            except ValueError:
                print('Ошибка введите число ')


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





