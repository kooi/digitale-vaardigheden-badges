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

# original objects
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

do_badge('green', 'lightgreen', 'turtle-green')
do_badge('midnightblue', 'lightblue', 'turtle-blue')
do_badge('maroon', 'bisque', 'turtle-red')
