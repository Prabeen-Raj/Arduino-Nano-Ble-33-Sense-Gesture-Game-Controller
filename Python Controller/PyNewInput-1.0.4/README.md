# PyDirectInput

This library aims to replicate the functionality of the PyDirectInput mouse and keyboard inputs, but by utilizing NewInput you can use the duration on moveTo(x, y, duration) and move(x, y, duration).

`pip install pynewinput`

## Documentation

The NewInput and DirectInput key codes are the same ones, https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input

You might also be interested in the main SendInput documentation here: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput

## Features Implemented

- Fail Safe Check
- Pause
- position()
- size()
- moveTo(x, y, duration)
- move(x, y, duration) / moveRel(x, y, duration)
- mouseDown()
- mouseUp()
- click()
- keyDown()
- keyUp()
- press()
- write() / typewrite()

## Features NOT Implemented

- scroll functions
- drag functions
- hotkey functions
- support for special characters requiring the shift key (ie. '!', '@', '#'...)
- ignored parameters on mouse functions: logScreenshot
- ignored parameters on keyboard functions: logScreenshot
