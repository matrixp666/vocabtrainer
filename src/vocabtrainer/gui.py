# coding: utf8
import PySimpleGUI as sg
import random

class gui(object):

    def __init__(self):
        sg.theme('BluePurple')
        self.vocab_eng = {}
        self.vocab_lat = {}
        self.shown_word = None
        self.translation = None

        with open('english.txt', 'r') as fh:
            content = fh.readlines()
            print(content)
        for line in content:
            eng, ger = line.split(';')
            eng = eng.strip(' ').strip('\n').strip('\r')
            ger = ger.strip(' ').strip('\n').strip('\r')
            if eng not in self.vocab_eng.keys():
                self.vocab_eng[eng] = ger
        with open('latein.txt', 'r') as fh:
            content = fh.readlines()
            print(content)
        for line in content:
            lat, ger = line.split(';')
            lat = lat.strip(' ').strip('\n').strip('\r')
            ger = ger.strip(' ').strip('\n').strip('\r')
            if lat not in self.vocab_lat.keys():
                self.vocab_lat[lat] = ger
        self.shown_word, self.translation = random.choice(list(self.vocab_eng.items()))
        self.layout = [
            [sg.Radio('English', 'lang', key = '-ENG-', enable_events = True, default = True), sg.Radio('Latein', 'lang', key = '-LAT-', enable_events = True, default = False)],
            [sg.Text('Uebersetze folgendes Wort nach Deutsch: {0}'.format(self.shown_word), key = '-LANG_TEXT-'), sg.Text(size = (15,1), key = '-OUTPUT-')],
            [sg.Input(key = '-IN-')],
            [sg.Button('Check', enable_events = True), sg.Button('Exit')],
                  ]

    def start_up(self):
        window = sg.Window('Vokabeltrainer', self.layout)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Check':
                print(self.translation)
                print(values['-IN-'])
                if values['-IN-'] == self.translation:
                    print('richtig')
                else:
                    print('ohohoh')
                window['-OUTPUT-'].update(self.shown_word)
                print('update')
            if event in ['-ENG-', '-LAT-']:
                if values['-ENG-'] == True:
                    self.cb_eng(values)
                    window['-LANG_TEXT-'].Update('Uebersetze folgendes Wort nach Deutsch: {0}'.format(self.shown_word))
                    
                if values['-ENG-'] == False:
                    self.cb_lat(values)
                    window['-LANG_TEXT-'].Update('Uebersetze folgendes Wort nach Deutsch: {0}'.format(self.shown_word))

        window.close()

    def cb_eng(self, values):
        print(self.translation)
        print(values['-IN-'])
        if values['-IN-'] == self.translation:
            print('richtig')
        else:
            print('ohohoh')


    def cb_lat(self, values):
        if values['-IN-'] == self.translation:
            print('richtig')
        else:
            print('ohohoh')

if __name__ == '__main__':
    gui = gui()
    gui.start_up()