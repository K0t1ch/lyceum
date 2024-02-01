import os
import sys

import pygame
import requests

mash_x = 0.002
mash_y = 0.002
dolg = -0.1245986
shir = 51.5006841

def draw(x, y, d, s):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={d},{s}&spn={x},{y}&l=sat"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    os.remove(map_file)


draw(mash_x, mash_y, dolg, shir)


pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if mash_x - 0.001 < 0.0:
                    pass
                else:
                    mash_x -= 0.001
                    mash_y -= 0.001
                    print(mash_x, mash_y)
                    draw(mash_x, mash_y, dolg, shir)
                    pygame.display.flip()

            elif event.key == pygame.K_PAGEDOWN:
                if mash_x + 0.001 > 0.008:
                    pass
                else:
                    mash_x += 0.001
                    mash_y += 0.001
                    print(mash_x, mash_y)
                    draw(mash_x, mash_y, dolg, shir)
                    pygame.display.flip()

            # ------------------------------------------------------------

            elif event.key == pygame.K_UP:
                if shir + 0.001 > 52.1:
                    pass
                else:
                    shir += 0.001
                    print(shir)
                    draw(mash_x, mash_y, dolg, shir)
                    pygame.display.flip()

            elif event.key == pygame.K_DOWN:
                if shir - 0.001 < 51.1:
                    pass
                else:
                    shir -= 0.001
                    print(shir)
                    draw(mash_x, mash_y, dolg, shir)
                    pygame.display.flip()

            # ------------------------------------------------------------

            elif event.key == pygame.K_LEFT:
                if dolg - 0.001 < -15.1:
                    pass
                else:
                    dolg -= 0.001
                    print(dolg)
                    draw(mash_x, mash_y, dolg, shir)
                    pygame.display.flip()

            elif event.key == pygame.K_RIGHT:
                if dolg + 0.001 > 0.01:
                    pass
                else:
                    dolg += 0.001
                    print(dolg)
                    draw(mash_x, mash_y, dolg, shir)
                    pygame.display.flip()


pygame.quit()
