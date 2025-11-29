from guizero import App, Box, Text, TextBox, PushButton, info

def dang_ky():
    ten = txt_ten_dang_nhap.value
    mk = txt_mat_khau.value
    if ten == "" or mk == "":
        info("Lỗi", "Nhập đủ tên và mật khẩu")
        return
    f = open("users.txt", "r")
    for dong in f:
        if dong.startswith(ten + ","):
            info("Lỗi", "Tên đã tồn tại")
            f.close()
            return
    f.close()
    f = open("users.txt", "a")
    f.write(ten + "," + mk + "\n")
    f.close()
    info("OK", "Đăng ký thành công")

def dang_nhap():
    ten = txt_ten_dang_nhap.value
    mk = txt_mat_khau.value
    f = open("users.txt", "r")
    for dong in f:
        if dong.startswith(ten + "," + mk):
            info("OK", "Đăng nhập thành công")
            f.close()
            return
    f.close()
    info("Sai", "Tên hoặc mật khẩu sai")

app = App("Đăng nhập / Đăng ký", width=350, height=180)

box_nut = Box(app, layout="grid")

Text(box_nut, "Đăng nhập / Đăng ký", grid=[0,0,2,1], size=14, align="top")
Text(box_nut, "Tên đăng nhập:", grid=[0,1], align="right")
txt_ten_dang_nhap = TextBox(box_nut, width=25, grid=[1,1])
Text(box_nut, "Mật khẩu:", grid=[0,2], align="right")
txt_mat_khau = TextBox(box_nut, width=25, hide_text=True, grid=[1,2])
PushButton(box_nut, text="Đăng nhập", grid=[0,3], width=12, command=dang_nhap)
PushButton(box_nut, text="Đăng ký", grid=[1,3], width=12, command=dang_ky)

app.display()
