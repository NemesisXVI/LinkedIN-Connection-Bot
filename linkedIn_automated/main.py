import pyautogui as pag
import images

pag.FAILSAFE = True


cell_num = str(input("cell num: "))
count = int(input("how many cells: "))

# opening chrome profiles

pag.hotkey("win", 'r',interval=0.25)
pag.countdown(1)
pag.typewrite("cmd",interval=0.02)
pag.countdown(1)
pag.hotkey("enter",interval=0.25)
pag.countdown(1)
pag.typewrite("start chrome",interval=0.02)
pag.countdown(1)
pag.hotkey("enter",interval=0.25)
pag.countdown(1)





pag.countdown(3)

# opening listing excel sheet
pag.hotkey("ctrl", 't')
pag.countdown(3)
pag.typewrite(images.listing_link, interval=0.08)
pag.countdown(1)
pag.press("enter")
pag.countdown(4)

# selecting cell num
pag.moveTo(x = (930,160), duration = 0.85)
pag.click()
pag.keyDown("ctrl")
pag.press('j')
pag.keyUp("ctrl")
pag.typewrite(cell_num, interval=0.1)
pag.press("enter")

while count>0:
    
    pag.countdown(3)
    pag.hotkey("ctrl", 'c')
    pag.countdown(2)
    pag.hotkey("ctrl", 't')
    pag.countdown(2)
    pag.hotkey("ctrl", 'v')
    pag.countdown(2)
    pag.press("enter")
    pag.countdown(10)

    #clicking connect button
    connect_button  = pag.locateCenterOnScreen(images.connect, confidence = 0.8,region = (50,50,1000,1000))
    connect2_button = pag.locateCenterOnScreen(images.connect2, confidence = 0.8,region = (50,50,1000,1000))
    more_button = pag.locateCenterOnScreen(images.more, confidence = 0.8,region = (50,50,1000,1000))
    pag.countdown(1)

    if connect_button:

        pag.moveTo(connect_button, duration = 0.8)
        pag.click()

    elif connect2_button:

        pag.moveTo(connect2_button, duration = 0.8)
        pag.click()

    else:

        pag.leftClick(more_button, duration = 0.6)
        more_connect_button = pag.locateCenterOnScreen(images.more_connect, confidence = 0.7)
        pag.moveTo(more_connect_button, duration = 0.2)
        pag.click()

    #going to message box
    pag.countdown(2)


    add_note_button = None
    while not add_note_button:
        pag.countdown(1)
        add_note_button = pag.locateCenterOnScreen(images.add_note, confidence = 0.8)
        pag.moveTo(add_note_button, duration = 0.57)
        pag.click()

    #typing message
    pag.countdown(1)
    pag.typewrite(images.marky_note, interval = 0.08)
    
    #sending message
    send_button = pag.locateCenterOnScreen(images.send, confidence = 0.9)
    send_button = pag.locateCenterOnScreen(images.without_note, confidence = 0.9)

    pag.moveTo(send_button, duration = 0.5)
    pag.click()

    #closing tab and going for next cell
    pag.countdown(3)
    pag.hotkey("ctrl", 'w')
    pag.countdown(3)
    pag.press("DOWN")

    count = count - 1
    print(f"CELLS remaining {count}")