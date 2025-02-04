from src.local_game import *from src.utilit import find_center_coordinatesfrom src.constants import *from random import choiceclass GlobalGame:    def __init__(self):        self.game_status = None        self.local_game_list = [LocalGame(find_center_coordinates(i, (WIDTH // 2 - SCALE // 2, HEIGHT // 2 - SCALE // 2), SCALE, k=3)) for i in range(9)]        self.whose_step = choice([1, -1])        self.accessible_local_games_indexes = [4]    def check_winner(self):        all_elem_indexes = [i for i in range(9) if self.local_game_list[i].game_status == self.whose_step]        for win_comb in WINNING_COMBINATIONS:            if win_comb[0] in all_elem_indexes and win_comb[1] in all_elem_indexes and win_comb[2] in all_elem_indexes:                self.game_status = self.whose_step                return None    def check_draw(self):        if self.game_status is None and len([i for i in self.local_game_list if i.game_status is None]) == 0:            self.game_status = 0 #means  a draw    def one_move(self, cursor_coordinates:tuple):        if cursor_coordinates is not None:            for local_game in self.local_game_list:                for i in local_game:                    if (i.get_coordinates()[0] < cursor_coordinates[0] <= i.get_coordinates()[0] + SCALE) and (i.get_coordinates()[1] < cursor_coordinates[1] <= i.get_coordinates()[1] + SCALE):                        if self.local_game_list.index(local_game) in self.accessible_local_games_indexes:                            if local_game.one_move(i.index, self.whose_step):                                self.check_winner()                                self.check_draw()                                self.whose_step *= -1                                if self.local_game_list[i.index].game_status is None:                                    self.accessible_local_games_indexes = [i.index]                                else:                                    self.accessible_local_games_indexes = []                                    for j in range(9):                                        if  self.local_game_list[j].game_status is None:                                            self.accessible_local_games_indexes.append(j)                                return None