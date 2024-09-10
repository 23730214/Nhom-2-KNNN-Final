import pygame
import random

pygame.init()

# Màu sắc cho game
trang = (255, 255, 255)
den = (0, 0, 0)
do = (255, 0, 0)
xam = (20, 20, 30)
vang = (255, 255, 0)
xanh_la = (0, 255, 0)
xanh_duong = (0, 0, 255)

# Thiết lập cửa sổ của game
chieu_rong_cua_so = 800
chieu_cao_cua_so = 600
cua_so = pygame.display.set_mode((chieu_rong_cua_so, chieu_cao_cua_so))
pygame.display.set_caption('Game Con Rắn - Nhóm 2')
font_tieng_viet = "NotoSans-Regular.ttf"
kieu_font = pygame.font.Font(font_tieng_viet, 30)

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
    pygame.draw.rect(cua_so, xanh_duong, [danh_sach_ran[-1][0], danh_sach_ran[-1][1], kich_thuoc_o_vuong, kich_thuoc_o_vuong])

# Tốc độ khung hình
dong_ho = pygame.time.Clock()
toc_do_ran = 15

# Danh sách rắn và chiều dài rắn
danh_sach_ran = []
chieu_dai_ran = 3

# Trạng thái trò chơi
tro_choi_ket_thuc = False
tro_choi_dong_cua = False
diem = 0

# Vòng lặp chính của trò chơi
while not tro_choi_ket_thuc:
    while tro_choi_dong_cua:
        cua_so.fill(xam)

        # Hiển thị thông báo thua
        thong_bao1 = kieu_font.render("Bạn đã thua! Nhấn Enter để chơi lại hoặc Space để thoát.", True, do)
        vi_tri_tin_nhan1 = thong_bao1.get_rect(center=(chieu_rong_cua_so / 2, chieu_cao_cua_so / 2 - 40))
        cua_so.blit(thong_bao1, vi_tri_tin_nhan1)
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

    # Cập nhật vị trí của rắn
    x1 += x1_thay_doi
    y1 += y1_thay_doi
    dau_ran = [x1, y1]

    # Nếu rắn chạm vào tường, trò chơi kết thúc
    if x1 >= chieu_rong_cua_so or x1 < 0 or y1 >= chieu_cao_cua_so or y1 < 0:
        tro_choi_dong_cua = True

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
    cua_so.fill(xam)
    pygame.draw.rect(cua_so, trang,
                     [kich_thuoc_khung_vien, kich_thuoc_khung_vien, chieu_rong_vung_choi, chieu_cao_vung_choi], 2)
    gia_tri_diem = kieu_font.render("Điểm: " + str(diem), True, vang)
    cua_so.blit(gia_tri_diem, [0, kich_thuoc_khung_vien / 2 - gia_tri_diem.get_height() / 2])

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

    pygame.display.update()

    # Tốc độ trò chơi
    dong_ho.tick(toc_do_ran)

pygame.quit()
quit()
