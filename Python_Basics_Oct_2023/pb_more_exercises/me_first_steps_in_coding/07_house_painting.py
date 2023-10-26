side_x = float(input())
side_y = float(input())
height = float(input())
GREEN_PAINT_PRICE = 3.4
RED_PAINT_PRICE = 4.3

square_walls_area = 2 * (side_x * side_x) - 1.2 * 2    # door
rectangle_walls_area = 2 * (side_x * side_y) - 2 * (1.5 * 1.5)    # window
green_paint_needed = square_walls_area + rectangle_walls_area
green_paint_total_price = green_paint_needed / GREEN_PAINT_PRICE

triangles_area = 2 * (side_x * height / 2)
roof_rectangles_area = 2 * (side_x * side_y)
red_paint_needed = triangles_area + roof_rectangles_area
red_paint_total_price = red_paint_needed / RED_PAINT_PRICE

print(f"{green_paint_total_price:.2f}")
print(f"{red_paint_total_price:.2f}")
