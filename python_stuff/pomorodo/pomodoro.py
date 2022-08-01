import PySimpleGUI as sg
from timer import Timer


sg.theme('DarkGray5')
timer = Timer('25')

layout = [

    [sg.Button("Focus"), sg.Button("Short Break"), sg.Button("Long Break")],
    timer.draw(),
    [sg.Button("Start"), sg.Button("Pause"), sg.Button("Stop")]

]

window = sg.Window('Pomodoro', layout)

start = False

while True:

    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break

    # timer mode change
    if event == "Focus":
        timer.minutes = '25'
        window['minutes'].update('25')
    elif event == "Short Break":
        timer.minutes = '5'
        window['minutes'].update('5')
    elif event == "Long Break":
        timer.minutes = '10'
        window['minutes'].update('10')

    # start the countdown
    if event == 'Start':
        event = sg.TIMEOUT_EVENT
        start = True

    if event == sg.TIMEOUT_EVENT:
        if int(window['minutes'].get()) >= 0:
            if int(window['seconds'].get()) > 0 and start:
                window['seconds'].update(int(window['seconds'].get()) - 1)
            elif int(window['seconds'].get()) == 0 and start:
                window['minutes'].update(int(window['minutes'].get()) - 1)
                window['seconds'].update('59')

