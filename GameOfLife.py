import pyglet
pyglet.resource.path = ['/Users/deewaiz/Downloads']
pyglet.resource.reindex()

# Задаем размерность поля
grid_size_x = 6
grid_size_y = 4

# Задаем толщину сетки
grid_width = 1

# Задаем размер ячейки
cell_size = 10

# Определяем и задаем размер окна
screen_width  = grid_size_x * (cell_size + 1) + 1
screen_height = grid_size_y * (cell_size + 1) + 1
print("x = ", screen_width, " y = ", screen_height)
window = pyglet.window.Window(screen_width, screen_height)
print("x = ", window.width, " y = ", window.height)



# Функция генерации игрового поля
def generate_grid():
    pyglet.gl.glColor3f(0.2, 1, 0.2)
    for x in range(1, window.width + 1, cell_size + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ("v2i", (x, 1, x, window.height))
                            )
    for y in range(0, window.height + 1, cell_size + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                             ("v2i", (1, y, window.width, y))
                            )

# Функция расположения клетки на игровом поле
def place_cell(x, y):
    pyglet.gl.glColor3f(1, 1, 1)
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 2, 1, 2, 3],
                                 ("v2i", (x * cell_size + x + 1,       y * cell_size + y + 1,
                                          x * cell_size + x + 1,       (y + 1) * cell_size + y + 1,
                                          (x + 1) * cell_size + x + 1, y * cell_size + y + 1,
                                          (x + 1) * cell_size + x + 1, (y + 1) * cell_size + y + 1))
                                 )


@window.event
def on_draw():
    window.clear()
    generate_grid()
    place_cell(0, 0)






    '''("v2i", (300, 300,
             300, 350,
             350, 300,
             350, 350))'''
pyglet.app.run()