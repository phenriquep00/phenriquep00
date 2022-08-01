import PySimpleGUI as sg

SIZE = [2, 1]
FONT = 'Any 30'


class Timer:
    def __init__(self, minutes):
        self.minutes = sg.Text(minutes, key='minutes', s=SIZE, font=FONT, justification='center',
                               background_color='#ffffff', text_color="#000000", p=20, relief="ridge", border_width=5)
        self.seconds = sg.Text('00', key='seconds', s=SIZE, font=FONT, justification='center',
                               background_color='#ffffff', text_color="#000000", p=20, relief="ridge", border_width=5)

    def draw(self):
        return [self.minutes, sg.Text(':', s=SIZE, font=FONT, justification='center',
                                      ), self.seconds]

