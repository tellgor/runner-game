import pygame


class Score:
    score_lst = [0, 0, 0, 0]  # (units, dozens, hundreds, thousands)
    frame_counter = 0  # variable  which counts frames for changing `score_lst`

    def __init__(self):
        self.screen = None
        self.font = pygame.font.Font(None, 65)
        self.score_units = self.font.render(str(Score.score_lst[0]), True, (255, 255, 255))
        self.score_dozens = self.font.render(str(Score.score_lst[1]), True, (255, 255, 255))
        self.score_hundreds = self.font.render(str(Score.score_lst[2]), True, (255, 255, 255))
        self.score_thousands = self.font.render(str(Score.score_lst[3]), True, (255, 255, 255))
        self.score_x = 850  # x cor for rendering on screen
        self.score_y = 10  # y cor for rendering on screen

    def score_increment(self):  # `Score.score_lst` growing algorithm
        Score.frame_counter += 1  # variable increase by 1 per frame
        if Score.frame_counter == 10:  # score increase by 1 per 10 frames
            Score.score_lst[0] += 1
            Score.frame_counter = 0
            for i in range(len(Score.score_lst)):  # loop through each index amd keep counting to increase each index individually
                if Score.score_lst[i] == 10 and Score.score_lst[i] != 3:
                    Score.score_lst[i+1] += 1
                    Score.score_lst[i] = 0
                else:
                    break

    def init(self, screen):  # initialization self.score_increment(), calculating position and rendering score
        self.score_increment()
        self.screen = screen
        tpl = (
            self.score_thousands, self.score_hundreds, self.score_dozens,
            self.score_units)  # tuple for loop implementation
        current_pos_x = self.score_x  # x cor for current index in score list
        pos_y = self.score_y  # y cor for all indexes in score list
        for i in range(len(tpl)):  # loop uses blit function for every index individually
            screen.blit(tpl[i], (current_pos_x, pos_y))
            current_pos_x += 28  # moves next index in loop by 28 pixels right

    @property
    def get_surfaces(self):  # getter for score tuple
        tpl = (self.score_thousands, self.score_hundreds, self.score_dozens, self.score_units)
        return tpl

    def restore(self):  # restoring class variables
        Score.score_lst = [0, 0, 0, 0]
        Score.frame_counter = 0
