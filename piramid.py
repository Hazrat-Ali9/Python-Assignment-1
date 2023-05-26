import pyautogui

def draw_pyramid(rows):
    screen_width, screen_height = pyautogui.size()
    x_offset = (screen_width - rows) // 2
    y_offset = (screen_height - rows) // 2

    for i in range(rows):
        num_blocks = 2 * i + 1
        x_pos = x_offset + (rows - i - 1)
        y_pos = y_offset + i

        pyautogui.moveTo(x_pos, y_pos)
        pyautogui.dragRel(num_blocks, 0, duration=0.1)

if __name__ == '__main__':
    num_rows = int(input("Enter the number of rows for the pyramid: "))
    draw_pyramid(num_rows)

