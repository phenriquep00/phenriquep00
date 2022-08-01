import PySimpleGUI as sg

sg.theme('DarkGray5')

layout = [
    [sg.Text('Pomodoro')],
    [],
    []
]

window = sg.Window('Pomodoro', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
