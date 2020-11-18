def RGBtoYUV(rgb):
    y = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    u = 0.492 * (rgb[1] - y)
    v = 0.877 * (rgb[0] - y)
    yuv = [y, u, v]

    return yuv


RGB = [1, 1, 1]

YUV = RGBtoYUV(RGB)
print(YUV)
