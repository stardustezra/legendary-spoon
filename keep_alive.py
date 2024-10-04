import pyautogui
import time

def keep_alive():
    try:
        while True:
            # Get the current mouse position
            current_mouse_position = pyautogui.position()

            # Move the mouse slightly to simulate activity
            pyautogui.moveRel(0, 1)  # Move the mouse down by 1 pixel
            time.sleep(0.5)
            pyautogui.moveRel(0, -1)  # Move the mouse back to the original position

            # Sleep for a few minutes before moving again
            time.sleep(300)  # 300 seconds = 5 minutes
            print("Mouse moved to simulate activity.")

    except KeyboardInterrupt:
        print("Program interrupted and stopped.")

if __name__ == "__main__":
    keep_alive()
