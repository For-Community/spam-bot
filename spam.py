import pyautogui
message=pyautogui.prompt(text="Text",title="DIORspammer")
while True:
    pyautogui.typewrite(message)
    pyautogui.press('enter')
