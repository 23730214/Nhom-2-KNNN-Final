import pygame
import random

pygame.init()

# Màu sắc trong game
trang = (255, 255, 255)
den = (0, 0, 0)
do = (255, 0, 0)
xam = (20, 20, 30)
vang = (255, 255, 0)
xanh_la = (96, 165, 111)
xanh_duong = (0, 0, 255)
xanh_duong_nhat = (226, 247, 184)
DarkOrange = (255, 140, 0)
Brown = (165, 42, 42)

# Thiết lập cửa sổ của game
chieu_rong_cua_so = 800
chieu_cao_cua_so = 600
cua_so = pygame.display.set_mode((chieu_rong_cua_so, chieu_cao_cua_so))
pygame.display.set_caption('Game Con Rắn - Nhóm 2')
font_tieng_viet = "FS-Ariston-Base.ttf"
kieu_font = pygame.font.Font(font_tieng_viet, 30)

tep_am_thanh = pygame.mixer.Sound('sounds/Snake_eat.wav')

# Vị trí ban đầu con rắn xuất hiện
x1 = chieu_rong_cua_so // 2
y1 = chieu_cao_cua_so // 2

# Kích thước ô vuông == con rắn
kich_thuoc_o_vuong = 10
kich_thuoc_khung_vien = 35
chieu_rong_vung_choi = chieu_rong_cua_so - 2 * kich_thuoc_khung_vien
chieu_cao_vung_choi = chieu_cao_cua_so - 2 * kich_thuoc_khung_vien

# Rắn di chuyển theo các bước pixel
x1_thay_doi = kich_thuoc_o_vuong
y1_thay_doi = 0

# Tạo mồi cho rắn với vị trí ngẫu nhiên trong vùng chơi
moi_x = round(random.randrange(kich_thuoc_khung_vien,
                               chieu_rong_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong) / kich_thuoc_o_vuong) * kich_thuoc_o_vuong
moi_y = round(random.randrange(kich_thuoc_khung_vien,
                               chieu_cao_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong) / kich_thuoc_o_vuong) * kich_thuoc_o_vuong


# Hàm để vẽ con rắn trên màn hình
def ve_ran(danh_sach_ran):
    for x in danh_sach_ran[:-1]:  # Vẽ thân rắn (trừ đầu)
        pygame.draw.rect(cua_so, xanh_la, [x[0], x[1], kich_thuoc_o_vuong, kich_thuoc_o_vuong])
    # Vẽ đầu rắn màu xanh dương để phân biệt
    pygame.draw.rect(cua_so, xanh_duong,
                     [danh_sach_ran[-1][0], danh_sach_ran[-1][1], kich_thuoc_o_vuong, kich_thuoc_o_vuong])


# Tốc độ khung hình
dong_ho = pygame.time.Clock()
toc_do_ran = 10

# Danh sách rắn và chiều dài rắn
danh_sach_ran = []
chieu_dai_ran = 3

# Trạng thái trò chơi
tro_choi_ket_thuc = False
tro_choi_dong_cua = False
tro_choi_bat_dau = False
diem = 0


def thong_bao(thong_diep, mau_sac):
    tin_nhan = kieu_font.render(thong_diep, True, mau_sac)   
    vi_tri_tin_nhan = tin_nhan.get_rect(
        center=(chieu_rong_cua_so / 2, chieu_cao_cua_so / 2))
    cua_so.blit(tin_nhan, vi_tri_tin_nhan)

while not tro_choi_bat_dau:
    cua_so.fill(DarkOrange)
    thong_bao("Nhấn một phím bất kỳ để bắt đầu", Brown)  # Hiển thị thông báo chờ
    pygame.display.update()

    # Xử lý các sự kiện
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            tro_choi_ket_thuc = True
            tro_choi_bat_dau = True
        if su_kien.type == pygame.KEYDOWN:
            tro_choi_bat_dau = True

# Vòng lặp chính của trò chơi
while not tro_choi_ket_thuc:
    while tro_choi_dong_cua:
        cua_so.fill(DarkOrange)

        # Hiển thị thông báo thua
        thong_bao1 = kieu_font.render("Bạn đã thua!", True, Brown)
        thong_bao2 = kieu_font.render("Điểm của bạn: " + str(diem), True, vang)
        thong_bao3 = kieu_font.render("Nhấn Enter để chơi lại hoặc Space để thoát", True, vang)

        vi_tri_tin_nhan1 = thong_bao1.get_rect(center=(chieu_rong_cua_so / 2, chieu_cao_cua_so / 2 - 40))
        vi_tri_tin_nhan2 = thong_bao2.get_rect(center=(chieu_rong_cua_so / 2, chieu_cao_cua_so / 2))
        vi_tri_tin_nhan3 = thong_bao3.get_rect(center=(chieu_rong_cua_so / 2, chieu_cao_cua_so / 2 + 40))

        cua_so.blit(thong_bao1, vi_tri_tin_nhan1)
        cua_so.blit(thong_bao2, vi_tri_tin_nhan2)
        cua_so.blit(thong_bao3, vi_tri_tin_nhan3)

        pygame.display.update()

        # Kiểm tra sự kiện phím khi trò chơi kết thúc
        for su_kien in pygame.event.get():
            if su_kien.type == pygame.QUIT:
                tro_choi_ket_thuc = True
                tro_choi_dong_cua = False
            if su_kien.type == pygame.KEYDOWN:
                if su_kien.key == pygame.K_RETURN:  # Nhấn Enter để chơi lại
                    tro_choi_dong_cua = False
                    x1 = chieu_rong_cua_so // 2
                    y1 = chieu_cao_cua_so // 2
                    x1_thay_doi = kich_thuoc_o_vuong
                    y1_thay_doi = 0
                    danh_sach_ran = []
                    chieu_dai_ran = 3
                    diem = 0
                    moi_x = round(random.randrange(kich_thuoc_khung_vien,
                                                   chieu_rong_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong) / kich_thuoc_o_vuong) * kich_thuoc_o_vuong
                    moi_y = round(random.randrange(kich_thuoc_khung_vien,
                                                   chieu_cao_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong) / kich_thuoc_o_vuong) * kich_thuoc_o_vuong
                elif su_kien.key == pygame.K_SPACE:  # Nhấn Space để thoát
                    tro_choi_ket_thuc = True
                    tro_choi_dong_cua = False

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

    # Kiểm tra va chạm với khung viền
    if x1 >= chieu_rong_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong or x1 < kich_thuoc_khung_vien or \
            y1 >= chieu_cao_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong or y1 < kich_thuoc_khung_vien:
        tro_choi_dong_cua = True  # Rắn va chạm với đường viền, kết thúc trò chơi

    # Cập nhật vị trí của rắn
    x1 += x1_thay_doi
    y1 += y1_thay_doi
    dau_ran = [x1, y1]

    # Thêm đầu rắn vào danh sách
    danh_sach_ran.append(dau_ran)

    # Xóa phần cuối của rắn nếu vượt quá chiều dài
    if len(danh_sach_ran) > chieu_dai_ran:
        del danh_sach_ran[0]

    # Kiểm tra va chạm với thân rắn
    for x in danh_sach_ran[:-1]:
        if x == dau_ran:
            tro_choi_dong_cua = True

    # Vẽ khung viền và điểm số
    cua_so.fill(xanh_duong_nhat)
    pygame.draw.rect(cua_so, Brown,
                     [kich_thuoc_khung_vien, kich_thuoc_khung_vien, chieu_rong_vung_choi, chieu_cao_vung_choi], 4)
    gia_tri_diem = kieu_font.render("Điểm: " + str(diem), True, Brown)
    cua_so.blit(gia_tri_diem, [10, kich_thuoc_khung_vien / 2 - gia_tri_diem.get_height() / 2])

    # Vẽ mồi
    pygame.draw.rect(cua_so, do, [moi_x, moi_y, kich_thuoc_o_vuong, kich_thuoc_o_vuong])

    # Vẽ rắn
    ve_ran(danh_sach_ran)

    # Kiểm tra nếu rắn ăn mồi
    if x1 == moi_x and y1 == moi_y:
        diem += 1
        moi_x = round(random.randrange(kich_thuoc_khung_vien,
                                       chieu_rong_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong) / kich_thuoc_o_vuong) * kich_thuoc_o_vuong
        moi_y = round(random.randrange(kich_thuoc_khung_vien,
                                       chieu_cao_cua_so - kich_thuoc_khung_vien - kich_thuoc_o_vuong) / kich_thuoc_o_vuong) * kich_thuoc_o_vuong
        chieu_dai_ran += 1
        tep_am_thanh.play()

    pygame.display.update()

    # Tốc độ trò chơi
    dong_ho.tick(toc_do_ran)

pygame.quit()
quit()