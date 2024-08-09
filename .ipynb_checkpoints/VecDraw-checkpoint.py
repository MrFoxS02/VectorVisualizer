import matplotlib.pyplot as plt
import numpy as np

class draw_2D_poligon:
       
    def __init__(self):
        self.x = []
        self.y = []
        
        self.ax_color = 'black'
        self.ax_bias = [0, 0]
        self.ax_width = [1, 1, 1, 1]
        self.ax_ls = '-'
        
    def get_vector(self, v:list, ends = True, ax_padding = 1, ax_lim = [0.2, 0.2, 0.2, 0.2], if_not_animation = True):
        self.x = [i[0] for i in v]
        self.y = [i[1] for i in v]
        
        if ends:
            self.x.append(self.x[0])
            self.y.append(self.y[0])
            
        if if_not_animation:   
            min_x, max_x = min(min(self.x), self.ax_width[0]) - ax_padding, max(max(self.x), self.ax_width[1]) + ax_padding
            min_y, max_y = min(min(self.y), self.ax_width[2]) - ax_padding, max(max(self.y), self.ax_width[3]) + ax_padding
        else:
            min_x, max_x = min(self.x) - ax_padding, max(self.x) + ax_padding
            min_y, max_y = min(self.y) - ax_padding, max(self.y) + ax_padding
        
        self.ax_width = [min_x, max_x, min_y, max_y]
        
        plt.xlim(self.ax_width[0] - ax_lim[0], self.ax_width[1] + ax_lim[1])
        plt.ylim(self.ax_width[2] - ax_lim[2], self.ax_width[3] + ax_lim[3])

    
    def draw_vector(self, end, start = (0, 0), color = 'black', alpha = 1, ls = '-', arrowstyle = '<-', 
                    text = '', text_color = 'black', text_bias = [0.2, 0.2]):
        bieses = [[1,1], [1,-1], [-1,1], [-1,-1], [0,1], [0,-1], [1,0], [-1,0]]
        arrowprops = {'arrowstyle': arrowstyle, 'color' : f'{color}', 'alpha' : alpha, 'linestyle' : ls}
        plt.annotate('', xy=start,xytext=end, arrowprops=arrowprops)
        if text != '':
            temp = list([int(x / x) if x != 0 else 0 for x in end])
            for i in range(len(end)):
                if end[i] < 0:
                    temp[i] *= -1 
            for bies in bieses:
                if temp == bies:
                    plt.text(end[0] + bies[0] * text_bias[0], end[1] + bies[1] * text_bias[1], s=text, color=text_color)
                    break
    
    def draw_axis(self, if_grid = False):
        self.draw_vector((self.ax_width[1], self.ax_bias[1]), start=(self.ax_width[0], self.ax_bias[1]), text='x', 
                        ls = self.ax_ls, color=self.ax_color)
        self.draw_vector((self.ax_bias[0], self.ax_width[3]), start=(self.ax_bias[0], self.ax_width[2]), text='y',
                        ls = self.ax_ls, color=self.ax_color)
        sc_x = [self.ax_width[1], self.ax_width[0], self.ax_bias[0], self.ax_bias[0]]
        sc_y = [self.ax_bias[1], self.ax_bias[1], self.ax_width[3], self.ax_width[2]]
        plt.scatter(sc_x, sc_y, s=1)
        if if_grid:
            plt.grid(True)
    
    def change_axis_params(self, ax_bias = [0, 0], ax_width = [1, 1, 1, 1], ax_color = 'black', ax_ls = '-', ax_lw = 1.5):
        if ax_width != [1, 1, 1, 1]:
            self.ax_width = ax_width 
        self.ax_color = ax_color 
        self.ax_bias = ax_bias 
        self.ax_ls = ax_ls 
        self.ax_lw = ax_lw
        
    def draw_poligon(self, color = 'blue', marker = None, ls = '-',  if_axis = False, if_grid = False):
        if if_axis:
            self.draw_axis()
        if if_grid:
            plt.grid(True)
        plt.plot(self.x, self.y, ls = ls, marker=marker, color=color)
        
    def draw_points(self, s=10, color = 'black', if_axis = False, if_grid = False):
        if if_axis:
            self.draw_axis()
        if if_grid:
            plt.grid(True)
        plt.scatter(self.x, self.y, color=color, s = s)
        
    def draw_segment(self, start = (0, 0), end = (1, 1), color = 'black', s = 10, lw = 1.5, ls = '-'):
        x = [start[0], end[0]]
        y = [start[1], end[1]]
        plt.scatter(x, y, color = color, s = s)
        plt.plot(x, y, color=color, lw = lw, ls = ls)