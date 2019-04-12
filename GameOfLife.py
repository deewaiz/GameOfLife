import pyglet
pyglet.resource.path = ['/Users/deewaiz/Downloads']
pyglet.resource.reindex()

# Задаем размерность поля
grid_size_x = 60
grid_size_y = 40

# Задаем толщину сетки
grid_width = 1

# Задаем размер ячейки
cell_size = 16

# Определяем и задаем размер окна
screen_width  = grid_size_x * (cell_size + 1) + 1
screen_height = grid_size_y * (cell_size + 1) + 1
print("x = ", screen_width, " y = ", screen_height)
window = pyglet.window.Window(screen_width, screen_height + 1)
print("x = ", window.width, " y = ", window.height)

# Генерируем игровое поле
def generate_grid():
    for x in range(1, window.width + 1, cell_size + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2i", (x, 1, x, window.height)))
    for y in range(1, window.height + 1, cell_size + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ("v2i", (1, y, window.width, y)))



@window.event
def on_draw():
    window.clear()
    generate_grid()

pyglet.app.run()