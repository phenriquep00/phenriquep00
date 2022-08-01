import PySimpleGUI as sg
from timer import Timer


def handle_time_decay(w):
    pass


sg.theme('DarkGray5')
timer = Timer('25')

layout = [

    [sg.Button("Focus"), sg.Button("Short Break"), sg.Button("Long Break")],
    timer.draw(),
    [sg.Button("Start"), sg.Button("Pause"), sg.Button("Stop")]

]

window = sg.Window('Pomodoro', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break

    if event == "Focus":
        timer.minutes = '25'
        window['minutes'].update('25')
    elif event == "Short Break":
        timer.minutes = '5'
        window['minutes'].update('5')
    elif event == "Long Break":
        timer.minutes = '10'
        window['minutes'].update('10')

    if event == 'Start':
        window['minutes'].update('24')
