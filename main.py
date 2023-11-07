def triangle():
    try:
          side_tr = float(input("Укажите сторону: "))
    except ValueError:
          return
    p_tr = 3 * side_tr
    s_tr = side_tr * side_tr * 1.73 / 4
    return p_tr, s_tr
p_per_tr, s_sp_tr = triangle()
print(f"Периметр треугольника = {p_per_tr}; Площадь треугольника = {s_sp_tr}")
