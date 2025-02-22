# addition.py
import pyautogui
import time
import subprocess

def perform_additional_tasks():
    """Perform additional tasks after URL pattern is detected."""
    # Wait for 2 seconds
    time.sleep(2)
    # Click on (290,180) and sleep for 2 seconds
    pyautogui.click(x=287, y=180)
    time.sleep(2)
    # Paste the extracted URL from xclip
    subprocess.run("xclip -o -selection clipboard | xargs xdotool type", shell=True)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)

if __name__ == "__main__":
    perform_additional_tasks()
