import pygame
from random import randrange as rnd


#создаем окно: задаём разрешение экрана, количество кадров, основной цикл
WIDTH, HEIGHT = 970, 600
nof = 60

#делаем перемещающийся прямоугольник
rect_w = 320 #ширина
rect_h = 40 #высота
rect_speed = 40 #скорость передвижения прямоугольника
#встраиваем экземпляр прямоугольник в класс Rect
#Rect работает с прямоугольниками установим: RECT=pygame.Rect(X1, Y1, W, H)
#Зададим атрибуты RECT: RECT.x=X1, RECT.y=Y1, RECT.w=W, RECT.h=H
#RECT.center=X,Y; RECT.centerx=X; RECT.centery=Y
#RECT.left=X1, RECT.right=X2, RECT.top=Y1, RECT.bottom=Y2
rect = pygame.Rect(WIDTH // 2 - rect_w // 2, HEIGHT - rect_h - 10, rect_w, rect_h)

# параметры шарика
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)#по стороне квадрата вписанного в окружность шара, используем при столкновении с обьектами
#экземпляр класса Rect
#размещение шарика рандомно по координате х, по y середина экрана
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1#направление движения, смена направления при столкновении


# расположение блоков
#размер 110*50, зазор между блоками 20, 10 от стены и до 1 блока; 4 ряда по 10 шт в каждом
#X=10+120*i; Y=10+70*j
blocks_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 110, 50) for i in range(10) for j in range(4)]
colors_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# фон
img = pygame.image.load('fon.jpeg').convert()


#определение столкновения
def collision_d(dx, dy, ball, rect):#вход коэффициентов x,y, экземпляр шарик и обьект на столкновение
    if dx > 0:#шар движется в право и сталкивается с левой стороной блока;
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:#ударяется в угол блока
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


while True:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            exit()
    sc.blit(img, (0, 0))#размещение фона на главной поверхности в начале координат

    # Рисуем обьекты
    [pygame.draw.rect(sc, colors_list[color], block) for color, block in enumerate(blocks_list)]#окрашиваем каждый блок в рамдомный цвет, через списковое включение и функции enumerate
    pygame.draw.rect(sc, pygame.Color('#F7FF00'), rect)#отображаем платформу,задаём цвет
    pygame.draw.circle(sc, pygame.Color('#EECDA3'), ball.center, ball_radius)#координаты центра шарика==координатам вписанного квадрата

    # движение шара
    ball.x += ball_speed * dx#по скорости и направлению движения
    ball.y += ball_speed * dy

    # определение границ для шара
    #столкновение с левой или правой стороной
    # расстояние от центра шарика между стороной меньше его радиуса изменяем напраление движения на противоположное
    #угол отражения==углу падения
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    # столкновение с потолком
    if ball.centery < ball_radius:
        dy = -dy
    # столкновение с прямоугольником
    if ball.colliderect(rect) and dy > 0:# возвращает True or False значение, в зависимости от столкновения
        dx, dy = collision_d(dx, dy, ball, rect)
    # столкновение с блоками
    collision_index = ball.collidelist(blocks_list)#возвращает индекс блока с которым было столкновение(-1 если столкновения нет)
    if collision_index != -1:
        collision_rect = blocks_list.pop(collision_index)#удаляем блок с которым столкнулись
        collision_color = colors_list.pop(collision_index)#удаляем его цвет
        dx, dy = collision_d(dx, dy, ball, collision_rect)
        # эффекты
        collision_rect.inflate_ip(ball.width * 3, ball.height * 3)#при столкновении квадрат увеличен
        pygame.draw.rect(sc, collision_color, collision_rect)#поднимаем скорость увеличивая количество кадров в секунду
        nof += 1
    # завершение игры
    if ball.bottom > HEIGHT:
        print('GAME OVER!')
        exit()
    elif not len(blocks_list):
        print('WIN!!!')
        exit()

    # управление
    #левый и правый край платформы не уходит за пределы экрана используя атрибуты класса React
    key = pygame.key.get_pressed()#движение платформы
    if key[pygame.K_LEFT] and rect.left > 0:
        rect.left -= rect_speed
    if key[pygame.K_RIGHT] and rect.right < WIDTH:
        rect.right += rect_speed

    # обновление экрана
    pygame.display.flip()
    clock.tick(nof)

