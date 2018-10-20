class Grid(object):
    def __init__(self):
        self.grid = [[0 for i in range(0, 5)] for j in range(0, 5)]

    def __str__(self):
        ret = ''
        for row in self.grid:
            ret += str((row)) + "\n"
        return ret


    def value_calc(self):
        steps = 10000
        alpha = 1.0
        gamma = 0.9
        for s in range(steps):
            for i in range(len(self.grid[0])):
                for j in range(len(self.grid[0])):
                    if i == 0 and j == 1:
                        reward = 10
                        self.grid[i][j] = alpha * (reward + gamma* self.grid[4][1])
                        continue
                    elif i == 0 and j == 3:
                        reward = 5
                        self.grid[i][j] = alpha * (reward + gamma * self.grid[2][3])
                        continue
                    else:
                        reward = reward_left = reward_up = reward_down = reward_right = 0
                    if j - 1 < 0:
                        left = self.grid[i][j]
                        reward_left = -1
                    else:
                        left = self.grid[i][j-1]
                    if i - 1 < 0:
                        up = self.grid[i][j]
                        reward_up = -1
                    else:
                        up = self.grid[i-1][j]
                    if j + 1 > 4:
                        right = self.grid[i][j]
                        reward_right = -1
                    else:
                        right = self.grid[i][j+1]
                    if i + 1 > 4:
                        down = self.grid[i][j]
                        reward_down = -1
                    else:
                        down = self.grid[i+1][j]

                    self.grid[i][j] = alpha * (
                        0.25 * (reward_left  + gamma * left) +
                        0.25 * (reward_right + gamma * right) +
                        0.25 * (reward_up    + gamma * up) +
                        0.25 * (reward_down  + gamma * down)
                    )

    def value_calc_terminal(self):
        steps = 10000
        alpha = 1.0
        gamma = 1.0
        for s in range(steps):
            for i in range(len(self.grid[0])):
                for j in range(len(self.grid[0])):
                    if i == 0 and j == 1:
                        continue
                        reward = 10
                        self.grid[i][j] = alpha * (reward + gamma* self.grid[4][1])
                    elif i == 0 and j == 3:
                        continue
                        reward = 5
                        self.grid[i][j] = alpha * (reward + gamma * self.grid[2][3])
                    else:
                        reward = reward_left = reward_up = reward_down = reward_right = 0

                    if j - 1 < 0:
                        left = self.grid[i][j]
                        reward_left = -1
                    else:
                        left = self.grid[i][j-1]
                    if i - 1 < 0:
                        up = self.grid[i][j]
                        reward_up = -1
                    else:
                        up = self.grid[i-1][j]
                    if j + 1 > 4:
                        right = self.grid[i][j]
                        reward_right = -1
                    else:
                        right = self.grid[i][j+1]
                    if i + 1 > 4:
                        down = self.grid[i][j]
                        reward_down = -1
                    else:
                        down = self.grid[i+1][j]

                    if i + 1 == 0 and j == 1:
                        reward_down = 10
                    elif i +1 == 0 and j == 3:
                        reward_down = 5

                    if i - 1 == 0 and j == 1:
                        reward_up = 10
                    elif i -1 == 0 and j == 3:
                        reward_up = 5

                    if i  == 0 and j -1  == 1:
                        reward_left = 10
                    elif i == 0 and j -1 == 3:
                        reward_left = 5

                    if i  == 0 and j +1  == 1:
                        reward_right = 10
                    elif i == 0 and j +1 == 3:
                        reward_right = 5

                    self.grid[i][j] = alpha * (
                        0.25 * (reward_left  + gamma * left) +
                        0.25 * (reward_right + gamma * right) +
                        0.25 * (reward_up    + gamma * up) +
                        0.25 * (reward_down  + gamma * down)
                    )

    def optimal_value_calc(self):
        steps = 10000
        alpha = 1.0
        gamma = 0.9
        for s in range(steps):
            for i in range(len(self.grid[0])):
                for j in range(len(self.grid[0])):
                    if i == 0 and j == 1:
                        reward = 10
                        self.grid[i][j] = alpha * (reward + gamma* self.grid[4][1])
                        continue
                    elif i == 0 and j == 3:
                        reward = 5
                        self.grid[i][j] = alpha * (reward + gamma * self.grid[2][3])
                        continue
                    else:
                        reward = reward_left = reward_up = reward_down = reward_right = 0
                    if j - 1 < 0:
                        left = self.grid[i][j]
                        reward_left = -1
                    else:
                        left = self.grid[i][j-1]
                    if i - 1 < 0:
                        up = self.grid[i][j]
                        reward_up = -1
                    else:
                        up = self.grid[i-1][j]
                    if j + 1 > 4:
                        right = self.grid[i][j]
                        reward_right = -1
                    else:
                        right = self.grid[i][j+1]
                    if i + 1 > 4:
                        down = self.grid[i][j]
                        reward_down = -1
                    else:
                        down = self.grid[i+1][j]

                    self.grid[i][j] = alpha * (
                        max([
                        reward_left  + gamma * left,
                        reward_right + gamma * right,
                        reward_up    + gamma * up, 
                        reward_down  + gamma * down
                        ])
                    )

    def optimal_value_calc_terminal(self):
        steps = 10000
        alpha = 1.0
        gamma = 1.0
        for s in range(steps):
            for i in range(len(self.grid[0])):
                for j in range(len(self.grid[0])):
                    if i == 0 and j == 1:
                        continue
                        reward = 10
                        self.grid[i][j] = alpha * (reward + gamma* self.grid[4][1])
                    elif i == 0 and j == 3:
                        continue
                        reward = 5
                        self.grid[i][j] = alpha * (reward + gamma * self.grid[2][3])
                    else:
                        reward = reward_left = reward_up = reward_down = reward_right = 0

                    if j - 1 < 0:
                        left = self.grid[i][j]
                        reward_left = -1
                    else:
                        left = self.grid[i][j-1]
                    if i - 1 < 0:
                        up = self.grid[i][j]
                        reward_up = -1
                    else:
                        up = self.grid[i-1][j]
                    if j + 1 > 4:
                        right = self.grid[i][j]
                        reward_right = -1
                    else:
                        right = self.grid[i][j+1]
                    if i + 1 > 4:
                        down = self.grid[i][j]
                        reward_down = -1
                    else:
                        down = self.grid[i+1][j]

                    if i + 1 == 0 and j == 1:
                        reward_down = 10
                    elif i +1 == 0 and j == 3:
                        reward_down = 5

                    if i - 1 == 0 and j == 1:
                        reward_up = 10
                    elif i -1 == 0 and j == 3:
                        reward_up = 5

                    if i  == 0 and j -1  == 1:
                        reward_left = 10
                    elif i == 0 and j -1 == 3:
                        reward_left = 5

                    if i  == 0 and j +1  == 1:
                        reward_right = 10
                    elif i == 0 and j +1 == 3:
                        reward_right = 5

                    self.grid[i][j] = alpha * (
                        max([
                        reward_left  + gamma * left,
                        reward_right + gamma * right,
                        reward_up    + gamma * up, 
                        reward_down  + gamma * down
                        ])
                    )




def main():
    grid = Grid()
    print(grid)
    # grid.value_calc()
    # grid.value_calc_terminal()
    # grid.optimal_value_calc()
    grid.optimal_value_calc_terminal()
    print(grid)
    pass

if __name__ == '__main__':
    main()
