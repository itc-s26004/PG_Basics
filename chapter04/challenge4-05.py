def box(x):
    """
    関数:box
    引数:x
    戻り値:xとfloat型のx
    """
    try:
        print(x)
        print(float(x))
        return x
    except ValueError:
        print("整数を入れてください")

x = str("6")
box(x)



