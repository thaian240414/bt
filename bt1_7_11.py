from guizero import App, Text, TextBox, PushButton, info

def dang_ky():
    ten = o_ten.value
    mk = o_mk.value
    if ten == "" or mk == "":
        info("Lỗi", "Nhập đủ thông tin")
        return
    f = open("users.txt", "r")
    for dong in f:
        dong = dong.strip()
        ten_file, mk_file = dong.split(",")
        if ten == ten_file:
            info("Lỗi", "Tên đã tồn tại")
            f.close()
            return
    f.close()
    f = open("users.txt", "a")
    f.write(ten + "," + mk + "\n")
    f.close()
    info("OK", "Đăng ký thành công")

def dang_nhap():
    ten = o_ten.value
    mk = o_mk.value
    f = open("users.txt", "r")
    for dong in f:
        dong = dong.strip()
        ten_file, mk_file = dong.split(",")
        if ten == ten_file and mk == mk_file:
            info("OK", "Đăng nhập thành công")
            f.close()
            return
    f.close()
    info("Sai", "Tên hoặc mật khẩu sai")

app = App("Đăng nhập / Đăng ký", width=300, height=220)

Text(app, "Đăng nhập / Đăng ký", size=16)
Text(app, "Tên đăng nhập:")
o_ten = TextBox(app, width=25)
Text(app, "Mật khẩu:")
o_mk = TextBox(app, width=25)
PushButton(app, text="Đăng nhập", width=20, command=dang_nhap)
PushButton(app, text="Đăng ký", width=20, command=dang_ky)

app.display()
