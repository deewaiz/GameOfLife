import pyglet
import random
import copy

# Таймер дисплея
fps_display = pyglet.clock.ClockDisplay()

# Статус игры
isStarted = False

# Задаем размерность поля
grid_size_x = 60
grid_size_y = 40

# Задаем размер ячейки
cell_size = 16

# Определяем и задаем размер окна
screen_width  = grid_size_x * (cell_size + 1) + 1
screen_height = grid_size_y * (cell_size + 1) + 1
window = pyglet.window.Window(screen_width, screen_height)

# Задаем массивы генераций клеток
first_gen_arr = []
second_gen_arr = []

# Метод генерации игрового поля
def generate_grid():
    pyglet.gl.glColor3f(0.2, 0.2, 0.2)
    for x in range(1, window.width + 1, cell_size + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ("v2i", (x, 1, x, window.height))
                            )
    for y in range(0, window.height + 1, cell_size + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ("v2i", (1, y, window.width, y))
                            )

# Метод расположения клетки на игровом поле
def place_cell(x, y):
    pyglet.gl.glColor3f(1, 1, 1)
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 1, 2, 3],
                                 ("v2i", (x * cell_size + x + 1,       y * cell_size + y + 1,
                                          x * cell_size + x + 1,       (y + 1) * cell_size + y + 1,
                                          (x + 1) * cell_size + x + 1, y * cell_size + y + 1,
                                          (x + 1) * cell_size + x + 1, (y + 1) * cell_size + y + 1))
                                 )

# Метод случайного заполнения поля и инициализации массивов генераций клеток
def random_fill_grid(chance): # 0 < chance < 100
    for i in range(grid_size_x):
        first_gen_arr.append([])
        second_gen_arr.append([])
        for j in range(grid_size_y):
            if random.random() * 100 <= chance:
                first_gen_arr[i].append(True)
                second_gen_arr[i].append(False)
                place_cell(i, j)
            else:
                first_gen_arr[i].append(False)
                second_gen_arr[i].append(False)

# Функция генерации пустого поля
def empty_fill_grid():
    for i in range(grid_size_x):
        first_gen_arr.append([])
        second_gen_arr.append([])
        for j in range(grid_size_y):
            first_gen_arr[i].append(False)
            second_gen_arr[i].append(False)

# Функция реализации бесконечности игрового поля по оси X
def infinity_x(x):
    if x > grid_size_x - 1:
        x = 0
        return x
    if x < 0:
        x = grid_size_x - 1
        return x
    return x

# Функция реализации бесконечности игрового поля по оси Y
def infinity_y(y):
    if y > grid_size_y - 1:
        y = 0
        return y
    if y < 0:
        y = grid_size_y - 1
        return y
    return y

# Функция считающая соседей
def neighbours_count(i, j):
    neighbours_count = 0
    if first_gen_arr[infinity_x(i - 1)][infinity_y(j - 1)] == True:
        neighbours_count += 1
    if first_gen_arr[infinity_x(i - 1)][infinity_y(j    )] == True:
        neighbours_count += 1
    if first_gen_arr[infinity_x(i - 1)][infinity_y(j + 1)] == True:
        neighbours_count += 1
    if first_gen_arr[infinity_x(i    )][infinity_y(j - 1)] == True:
        neighbours_count += 1
    if first_gen_arr[infinity_x(i    )][infinity_y(j + 1)] == True:
        neighbours_count += 1
    if first_gen_arr[infinity_x(i + 1)][infinity_y(j - 1)] == True:
        neighbours_count += 1
    if first_gen_arr[infinity_x(i + 1)][infinity_y(j    )] == True:
        neighbours_count += 1
    if first_gen_arr[infinity_x(i + 1)][infinity_y(j + 1)] == True:
        neighbours_count += 1
    return neighbours_count

# Функция расположения глайдера
def place_glider(x, y):
    first_gen_arr[x    ][y    ] = True
    first_gen_arr[x + 1][y    ] = True
    first_gen_arr[x + 2][y    ] = True
    first_gen_arr[x + 2][y + 1] = True
    first_gen_arr[x + 1][y + 2] = True

    place_cell(x    , y    )
    place_cell(x + 1, y    )
    place_cell(x + 2, y    )
    place_cell(x + 2, y + 1)
    place_cell(x + 1, y + 2)

@window.event
def on_draw():
    global isStarted, first_gen_arr, second_gen_arr
    window.clear()
    fps_display.draw()

    generate_grid()

    # Инициализация игры
    if isStarted == False:
        random_fill_grid(20)
        #empty_fill_grid()
        #place_glider(int(grid_size_x / 2), int(grid_size_y / 2))
        isStarted = True

    # Запуск основного цикла программы
    else:
        # Отрисовка генерации клеток
        for i in range(grid_size_x):
            for j in range(grid_size_y):
                if first_gen_arr[i][j] == True:
                    place_cell(i, j)

    # Основная логика
    for i in range(grid_size_x):
        for j in range(grid_size_y):

            if first_gen_arr[i][j] == False and neighbours_count(i, j) == 3:
                second_gen_arr[i][j] = True

            if first_gen_arr[i][j] == True and (neighbours_count(i, j) < 2 or neighbours_count(i, j) > 3):
                second_gen_arr[i][j] = False

    # Заносим изменения в первый массив
    first_gen_arr = copy.deepcopy(second_gen_arr)

pyglet.app.run()