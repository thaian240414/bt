from guizero import App, Box, Text, TextBox, Combo, Drawing, Slider, PushButton

app = App(title="Meme Creator", width=650, height=650)

# ===== KHUNG TRÊN (ĐIỀU KHIỂN) =====
control_box = Box(app, width="fill", border=True)

Text(control_box, text="MEME CREATOR", size=18, color="blue")

Text(control_box, text="Nội dung:")
input_text = TextBox(control_box, width=40)

row1 = Box(control_box, layout="grid")
Text(row1, text="Màu chữ:", grid=[0,0])
color_box = Combo(row1, options=["black", "white", "red", "yellow"], grid=[1,0])

Text(row1, text="Font:", grid=[2,0])
font_box = Combo(row1, options=["Arial", "Times New Roman", "Courier"], grid=[3,0])

row2 = Box(control_box, layout="grid")
Text(row2, text="X:", grid=[0,0])
x_slider = Slider(row2, start=0, end=400, grid=[1,0])

Text(row2, text="Y:", grid=[2,0])
y_slider = Slider(row2, start=0, end=300, grid=[3,0])

# ===== KHUNG DƯỚI (ẢNH) =====
drawing = Drawing(app, width=500, height=350)
drawing.image(0, 0, "meme.png")

def draw_text():
    drawing.clear()
    drawing.image(0, 0, "meme.png")

    drawing.text(
        x_slider.value,
        y_slider.value,
        input_text.value,
        color=color_box.value,
        font=font_box.value,
        size=20
    )

    # Lưu file
    with open("cau1.txt", "w", encoding="utf-8") as f:
        f.write(input_text.value)

PushButton(app, text="THÊM CHỮ & LƯU", command=draw_text)

app.display()
