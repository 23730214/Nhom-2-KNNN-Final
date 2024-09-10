import pygame

pygame.init()

xanh_duong = (0, 0, 255)

font_tieng_viet = "NotoSans-Regular.ttf"
kieu_font = pygame.font.Font(font_tieng_viet, 30)

chieu_rong_cua_so = 800
chieu_cao_cua_so = 600
cua_so = pygame.display.set_mode((chieu_rong_cua_so, chieu_cao_cua_so))
pygame.display.set_caption("Rắn Săn Mồi - Nhóm 2")

tro_choi_ket_thuc=False
while not tro_choi_ket_thuc:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            tro_choi_ket_thuc=True
    pygame.draw.rect(cua_so,xanh_duong,[200,150,10,10])
    pygame.display.update()
pygame.quit()
quit()