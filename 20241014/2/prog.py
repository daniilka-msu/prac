from math import *


def scale_value(src_min, src_max, target_min, target_max, value):
    return (value - src_min) * (target_max - target_min) / (src_max - src_min) + target_min


def print_graph(screen):
    print('\n'.join(''.join(line) for line in screen))


def plot_graph(width, height, x_min, x_max, expression):
    canvas = [[' '] * width for _ in range(height)]
    x_values = list(range(width))
    x_mapped = [scale_value(0, width - 1, x_min, x_max, x) for x in x_values]
    y_values = list(map(lambda x: eval(expression), x_mapped))
    y_mapped = []

    for y in y_values:
        scaled_y = scale_value(min(y_values), max(y_values), 0, height - 1, y)
        y_mapped.append(ceil(scaled_y) if scaled_y - int(scaled_y) >= 0.5 else floor(scaled_y))

    for x, y in zip(x_values, y_mapped):
        canvas[height - y - 1][x] = '*'

    for col in range(width):
        column = [canvas[row][col] for row in range(height)]
        if column.count('*') > 1:
            indices = [i for i, value in enumerate(column) if value == '*']
            for j in range(indices[0], indices[-1]):
                canvas[j][col] = "*"

    for col in range(width - 1):
        current_col = [canvas[row][col] for row in range(height)]
        next_col = [canvas[row][col + 1] for row in range(height)]
        next_col_last = ''.join(next_col).rfind('*')
        next_col_first = ''.join(next_col).find('*')
        current_col_last = ''.join(current_col).rfind('*')
        current_col_first = ''.join(current_col).find('*')

        if current_col_first > next_col_last:
            for i in range(next_col_last + 1, current_col_first):
                canvas[i][col] = "*"
        if current_col_last < next_col_first:
            for i in range(current_col_last + 1, next_col_first):
                canvas[i][col + 1] = "*"

    return canvas


parameters = input().split()
width, height, x_min, x_max, expression = int(parameters[0]), int(parameters[1]), int(parameters[2]), int(parameters[3]), parameters[4]
print_graph(plot_graph(width, height, x_min, x_max, expression))

