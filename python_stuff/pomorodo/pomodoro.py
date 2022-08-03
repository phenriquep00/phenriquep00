import PySimpleGUI as sg
from timer import Timer


sg.theme('DarkGray5')
timer = Timer('24')

layout = [

    [sg.Button("Focus"), sg.Button("Short Break"), sg.Button("Long Break")],
    [sg.Button("+", s=(3, 1)), sg.Button("-", s=(3, 1))],
    timer.draw(),
    [sg.Button("Start", s=(5, 1)), sg.Button("Pause", s=(5, 1)), sg.Button("Stop", s=(5, 1))]

]

window = sg.Window('Pomodoro', layout)

start = False

while True:

    event, values = window.read(timeout=1000)

    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break

    # timer mode change
    if event == "Focus":
        timer.minutes = '24'
        window['minutes'].update('24')
    elif event == "Short Break":
        timer.minutes = '4'
        window['minutes'].update('4')
    elif event == "Long Break":
        timer.minutes = '9'
        window['minutes'].update('9')

    # + - buttons
    if event == "+":
        timer.minutes = int(window['minutes'].get()) + 1
        window['minutes'].update(timer.minutes)
    if event == "-" and int(timer.minutes) > 0:
        timer.minutes = int(window['minutes'].get()) - 1
        window['minutes'].update(timer.minutes)

    # start the countdown
    if event == 'Start' and not start:
        event = sg.TIMEOUT_EVENT
        start = True

    if event == 'Pause':
        start = False

    if event == 'Stop':
        start = False
        timer.minutes = '24'
        timer.seconds = '59'
        window['seconds'].update('59')
        window['minutes'].update('24')

    if event == sg.TIMEOUT_EVENT:
        if int(window['minutes'].get()) >= 0:
            if int(window['seconds'].get()) > 0 and start:
                window['seconds'].update(int(window['seconds'].get()) - 1)
            elif int(window['seconds'].get()) == 0 and start:
                window['minutes'].update(int(window['minutes'].get()) - 1)
                window['seconds'].update('59')
