import PySimpleGUI as sg

sg.theme('DarkGray5')

layout = [
    [sg.Text('Pomodoro')],
    [sg.Button("Focus"), sg.Button("Short Break"), sg.Button("Long Break")],
    [sg.Text("25"), sg.Text(":"), sg.Text("00")],
    [sg.Button("Start")]
]

window = sg.Window('Pomodoro', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break

