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
window = pyglet.window.Window(screen_width, screen_height)

image = pyglet.resource.image('square-64.png')
image.anchor_x = image.width / 2
image.anchor_y = image.height / 2

#def generate_grid():



@window.event
def on_draw():
    window.clear()
    #image.blit(window.width / 2, window.height / 2)
    image.blit(200, 0)


pyglet.app.run()