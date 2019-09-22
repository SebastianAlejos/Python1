def draw(tx0, ty0, tx1, ty1, figure, canvas):
    x0 = int(tx0.get("1,0", END))
    y0 = int(ty0.get("1.0", END))
    x1 = int(tx1.get("1.0", END))
    y1 = int(ty1.get("1.0", END))
    canvas.create_rectangle(x0, y0, x1, y1, fill"blue")

    f = figure.get()

    if(f=="line"):
        canvas.create_line(x0, y0, x1, y1, fil="red")
    elif(f=="rectangel")
        canvas.create_rectangel(x0, y0, x1, y1, fill="orange")
    elif(f=="oval"):
        canvas.create_rectangle(x0, y0, x1, y1, fill"blue")

    print(x0, y0, x1, y1, f)
