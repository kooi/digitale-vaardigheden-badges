import svg_polygons

# mirror
def mirrorx(list):
    list2 = []
    for i,j in list:
        list2.append( ( -1 * i, j) )
    return list2

def mirrory(list):
    list2 = []
    for i,j in list:
        list2.append( ( i, -1 * j) )
    return list2

# rescale
def scale(list, scale):
    list2 = []
    for i,j in list:
        list2.append( ( scale*i, scale*j) )
    return list2


# use center as last for transformation purposes
def center(list, x_offset, y_offset):
    list2 = []
    for i,j in list:
        list2.append( ( i+x_offset, j+y_offset) )
    return list2


def bbox(list):
    minx = list[0][0]
    miny = list[0][1]
    maxx = list[0][0]
    maxy = list[0][1]
    for x, y in list:
        if x > maxx:
            maxx = x
        if x < minx:
            minx = x
        if y > maxy:
            maxy = y
        if y < miny:
            miny = y
    return [ (minx, miny), (maxx, miny), (maxx, maxy), (minx, maxy), (minx, miny) ]

# original objects, exported from turtle using begin_poly(), end_poly() and getpoly()
sierpinski_arrowhead_curve_order_5_length_128 = [(0.00,0.00), (2.00,-3.46), (6.00,-3.46), (8.00,0.00), (12.00,0.00), (14.00,-3.46), (12.00,-6.93), (8.00,-6.93), (6.00,-10.39), (8.00,-13.86), (12.00,-13.86), (14.00,-17.32), (12.00,-20.78), (14.00,-24.25), (18.00,-24.25), (20.00,-20.78), (18.00,-17.32), (20.00,-13.86), (24.00,-13.86), (26.00,-10.39), (24.00,-6.93), (20.00,-6.93), (18.00,-3.46), (20.00,0.00), (24.00,0.00), (26.00,-3.46), (30.00,-3.46), (32.00,0.00), (36.00,0.00), (38.00,-3.46), (36.00,-6.93), (38.00,-10.39), (42.00,-10.39), (44.00,-6.93), (42.00,-3.46), (44.00,0.00), (48.00,0.00), (50.00,-3.46), (54.00,-3.46), (56.00,0.00), (60.00,0.00), (62.00,-3.46), (60.00,-6.93), (56.00,-6.93), (54.00,-10.39), (56.00,-13.86), (54.00,-17.32), (50.00,-17.32), (48.00,-13.86), (44.00,-13.86), (42.00,-17.32), (44.00,-20.78), (48.00,-20.78), (50.00,-24.25), (48.00,-27.71), (44.00,-27.71), (42.00,-31.18), (44.00,-34.64), (42.00,-38.11), (38.00,-38.11), (36.00,-34.64), (38.00,-31.18), (36.00,-27.71), (32.00,-27.71), (30.00,-31.18), (26.00,-31.18), (24.00,-27.71), (20.00,-27.71), (18.00,-31.18), (20.00,-34.64), (24.00,-34.64), (26.00,-38.11), (24.00,-41.57), (26.00,-45.03), (30.00,-45.03), (32.00,-41.57), (36.00,-41.57), (38.00,-45.03), (36.00,-48.50), (32.00,-48.50), (30.00,-51.96), (32.00,-55.43), (36.00,-55.43), (38.00,-58.89), (36.00,-62.35), (38.00,-65.82), (42.00,-65.82), (44.00,-62.35), (42.00,-58.89), (44.00,-55.43), (48.00,-55.43), (50.00,-58.89), (54.00,-58.89), (56.00,-55.43), (60.00,-55.43), (62.00,-58.89), (60.00,-62.35), (56.00,-62.35), (54.00,-65.82), (56.00,-69.28), (54.00,-72.75), (50.00,-72.75), (48.00,-69.28), (44.00,-69.28), (42.00,-72.75), (44.00,-76.21), (48.00,-76.21), (50.00,-79.67), (48.00,-83.14), (50.00,-86.60), (54.00,-86.60), (56.00,-83.14), (60.00,-83.14), (62.00,-86.60), (60.00,-90.07), (56.00,-90.07), (54.00,-93.53), (56.00,-96.99), (60.00,-96.99), (62.00,-100.46), (60.00,-103.92), (62.00,-107.39), (66.00,-107.39), (68.00,-103.92), (66.00,-100.46), (68.00,-96.99), (72.00,-96.99), (74.00,-93.53), (72.00,-90.07), (68.00,-90.07), (66.00,-86.60), (68.00,-83.14), (72.00,-83.14), (74.00,-86.60), (78.00,-86.60), (80.00,-83.14), (78.00,-79.67), (80.00,-76.21), (84.00,-76.21), (86.00,-72.75), (84.00,-69.28), (80.00,-69.28), (78.00,-72.75), (74.00,-72.75), (72.00,-69.28), (74.00,-65.82), (72.00,-62.35), (68.00,-62.35), (66.00,-58.89), (68.00,-55.43), (72.00,-55.43), (74.00,-58.89), (78.00,-58.89), (80.00,-55.43), (84.00,-55.43), (86.00,-58.89), (84.00,-62.35), (86.00,-65.82), (90.00,-65.82), (92.00,-62.35), (90.00,-58.89), (92.00,-55.43), (96.00,-55.43), (98.00,-51.96), (96.00,-48.50), (92.00,-48.50), (90.00,-45.03), (92.00,-41.57), (96.00,-41.57), (98.00,-45.03), (102.00,-45.03), (104.00,-41.57), (102.00,-38.11), (104.00,-34.64), (108.00,-34.64), (110.00,-31.18), (108.00,-27.71), (104.00,-27.71), (102.00,-31.18), (98.00,-31.18), (96.00,-27.71), (92.00,-27.71), (90.00,-31.18), (92.00,-34.64), (90.00,-38.11), (86.00,-38.11), (84.00,-34.64), (86.00,-31.18), (84.00,-27.71), (80.00,-27.71), (78.00,-24.25), (80.00,-20.78), (84.00,-20.78), (86.00,-17.32), (84.00,-13.86), (80.00,-13.86), (78.00,-17.32), (74.00,-17.32), (72.00,-13.86), (74.00,-10.39), (72.00,-6.93), (68.00,-6.93), (66.00,-3.46), (68.00,-0.00), (72.00,-0.00), (74.00,-3.46), (78.00,-3.46), (80.00,-0.00), (84.00,-0.00), (86.00,-3.46), (84.00,-6.93), (86.00,-10.39), (90.00,-10.39), (92.00,-6.93), (90.00,-3.46), (92.00,-0.00), (96.00,-0.00), (98.00,-3.46), (102.00,-3.46), (104.00,-0.00), (108.00,-0.00), (110.00,-3.46), (108.00,-6.93), (104.00,-6.93), (102.00,-10.39), (104.00,-13.86), (108.00,-13.86), (110.00,-17.32), (108.00,-20.78), (110.00,-24.25), (114.00,-24.25), (116.00,-20.78), (114.00,-17.32), (116.00,-13.86), (120.00,-13.86), (122.00,-10.39), (120.00,-6.93), (116.00,-6.93), (114.00,-3.46), (116.00,-0.00), (120.00,-0.00), (122.00,-3.46), (126.00,-3.46), (128.00,-0.00)]


rounded_hex_border = [(0.00,0.00), (100.00,0.00), (100.99,0.10), (101.97,0.31), (102.92,0.62), (103.84,1.03), (104.70,1.53), (105.51,2.12), (106.26,2.79), (106.92,3.53), (107.51,4.34), (108.01,5.20), (158.01,91.81), (158.42,92.72), (158.73,93.67), (158.94,94.65), (159.04,95.64), (159.04,96.64), (158.94,97.64), (158.73,98.62), (158.42,99.57), (158.01,100.48), (157.51,101.35), (107.51,187.95), (106.92,188.76), (106.26,189.50), (105.51,190.17), (104.70,190.76), (103.84,191.26), (102.92,191.66), (101.97,191.97), (100.99,192.18), (100.00,192.29), (99.00,192.29), (-1.00,192.29), (-1.99,192.18), (-2.97,191.97), (-3.92,191.66), (-4.84,191.26), (-5.70,190.76), (-6.51,190.17), (-7.26,189.50), (-7.92,188.76), (-8.51,187.95), (-9.01,187.08), (-59.01,100.48), (-59.42,99.57), (-59.73,98.62), (-59.94,97.64), (-60.04,96.64), (-60.04,95.64), (-59.94,94.65), (-59.73,93.67), (-59.42,92.72), (-59.01,91.81), (-58.51,90.94), (-8.51,4.34), (-7.92,3.53), (-7.26,2.79), (-6.51,2.12), (-5.70,1.53), (-4.84,1.03), (-3.92,0.62), (-2.97,0.31), (-1.99,0.10), (-1.00,0.00), (0.00,0.00)]
hex_badge_border = [(0.00,0.00), (100.00,0.00), (150.00,86.60), (100.00,173.21), (0.00,173.21), (-50.00,86.60), (-0.00,0.00)]
badge_border = [(0.00,0.00), (100.00,0.00), (150.00,86.60), (100.00,173.21), (0.00,173.21), (-50.00,86.60), (-0.00,0.00)]
turtle = [(0, 16), (-2, 14), (-1, 10), (-4, 7), (-7, 9), (-9, 8), (-6, 5), (-7, 1), (-5, -3), (-8, -6), (-6, -8), (-4, -5), (0, -7), (4, -5), (6, -8), (8, -6), (5, -3), (7, 1), (6, 5), (9, 8), (7, 9), (4, 7), (1, 10), (2, 14)]

# transforms
badge_border2 = scale(rounded_hex_border, 0.8)
badge_border2 = center(badge_border2, 210, 190)
badge_border3 = scale(rounded_hex_border, 0.9)
badge_border3 = center(badge_border3, 205, 180)

turtle3 = mirrory(turtle)
turtle3 = scale(turtle3, 5.0)
turtle3 = center(turtle3, 250, 285)

# drawing_template
def do_badge(c1, c2, filename):
    my_drawing = svg_polygons.Canvas(500, 500)
    my_drawing.polygon(badge_border3, c1, c1, 1.0 )
    my_drawing.polygon(badge_border2, c1, c2, 1.0 )
    my_drawing.polygon(turtle3, 'green', 'lawngreen', 1.0)
    #my_drawing.polygon(bbox(turtle3), 'blue', None, 1.0)
    # export
    my_drawing.save(filename)

def export_poly(poly, color1, color2, filename):
    my_drawing = svg_polygons.Canvas(500, 500)
    my_drawing.polygon(poly, color1, color2, 1.0 )
    my_drawing.save(filename)

#do_badge('green', 'lightgreen', 'turtle-green')
#do_badge('midnightblue', 'lightblue', 'turtle-blue')
#do_badge('maroon', 'bisque', 'turtle-red')

export_poly(sierpinski_arrowhead_curve_order_5_length_128, 'black', 'black', 'sierpinski_arrowhead_curve')
