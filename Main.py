import pygame

pygame.init()

# // Lam mau sac cho game
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# # Thiet lap cua so cua game
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Game Con Rắn - Nhóm 2')

# set trang thái bằng false 
game_over = False

# vị trí ban đầu con rắn xuất hiện
x1 = dis_width // 2
y1 = dis_height // 2

# kích thước o vuong == con ran
kich_thuoc_o_vuong = 10

# rắn di chuyển theo các bước pixel
x1_thay_doi = kich_thuoc_o_vuong
y1_thay_doi = 0


#tốc độ khung hình
clock = pygame.time.Clock()
snake_speed = 15

# vòng lặp chính của trò chơi
while not game_over:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            tro_choi_ket_thuc = True 
        if su_kien.type == pygame.KEYDOWN: 
            if su_kien.key == pygame.K_LEFT and x1_thay_doi == 0:  
                x1_thay_doi = -kich_thuoc_o_vuong
                y1_thay_doi = 0
            elif su_kien.key == pygame.K_RIGHT and x1_thay_doi == 0:
                x1_thay_doi = kich_thuoc_o_vuong
                y1_thay_doi = 0
            elif su_kien.key == pygame.K_UP and y1_thay_doi == 0: 
                y1_thay_doi = -kich_thuoc_o_vuong
                x1_thay_doi = 0
            elif su_kien.key == pygame.K_DOWN and y1_thay_doi == 0:
                y1_thay_doi = kich_thuoc_o_vuong
                x1_thay_doi = 0

    # cập nhật vị trí của rắn
    x1 += x1_thay_doi
    y1 += y1_thay_doi

    # nếu rắn chạm vào tường thì kết thúc trò chơi
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    # màn hình và rắn
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, kich_thuoc_o_vuong, kich_thuoc_o_vuong])

    pygame.display.update()

    # tốc độ trò chơi
    clock.tick(snake_speed)

pygame.quit()
quit()
