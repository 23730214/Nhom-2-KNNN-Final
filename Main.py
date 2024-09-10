import pygame

pygame.init()

# // Lam mau sac cho game
trang = (255, 255, 255)
den = (0, 0, 0)
do = (255, 0, 0)

# # Thiet lap cua so cua game
chieu_rong_cua_so = 800
chieu_cao_cua_so = 600
cua_so = pygame.display.set_mode((chieu_rong_cua_so, chieu_cao_cua_so))
pygame.display.set_caption('Game Con Rắn - Nhóm 2')

# set trang thái bằng false 
tro_choi_ket_thuc = False

# vị trí ban đầu con rắn xuất hiện
x1 = chieu_rong_cua_so // 2
y1 = chieu_cao_cua_so // 2

# kích thước o vuong == con ran
kich_thuoc_o_vuong = 10

# rắn di chuyển theo các bước pixel
x1_thay_doi = kich_thuoc_o_vuong
y1_thay_doi = 0


#tốc độ khung hình
dong_ho = pygame.time.Clock()
toc_do_ran = 15

# vòng lặp chính của trò chơi
while not tro_choi_ket_thuc:
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
    if x1 >= chieu_rong_cua_so or x1 < 0 or y1 >= chieu_cao_cua_so or y1 < 0:
        game_over = True

    # màn hình và rắn
    cua_so.fill(trang)
    pygame.draw.rect(cua_so, den, [x1, y1, kich_thuoc_o_vuong, kich_thuoc_o_vuong])

    pygame.display.update()

    # tốc độ trò chơi
    dong_ho.tick(toc_do_ran)

pygame.quit()
quit()
