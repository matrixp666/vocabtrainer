# coding: utf8
import PySimpleGUI as sg
import random
import os

class gui(object):

    def __init__(self):
        sg.theme('BluePurple')
        self.vocab_eng = {}
        self.vocab_lat = {}
        self.shown_word = None
        self.translation = None
        self.cnter_correct = 0
        self.cnter_incorrect = 0

        self.read_translation_files()
        self.shown_word, self.translation = random.choice(list(self.vocab_eng.items()))
        self.layout = [
            [sg.Radio('English', 'lang', key = '-ENG-', enable_events = True, default = True), sg.Radio('Latein', 'lang', key = '-LAT-', enable_events = True, default = False)],
            [sg.Text('Uebersetze folgendes Wort nach Deutsch: ', key = '-LANG_TEXT-'), sg.Text(text = self.shown_word, size = (15,1), key = '-OUTPUT-')],
            [sg.Input(key = '-IN-')],
            [sg.Button('Check', enable_events = True, key = '-CHECK-'), sg.Button('Exit')],
            [sg.HorizontalSeparator()],
            [sg.Text('Anzahl richtiger und falscher Antworten:')],
            [sg.Text('Richtige:'), sg.Text(key='-CORRECT-')],
            [sg.Text('Falsche:'), sg.Text(key='-INCORRECT-')],
                  ]

    def read_translation_files(self):
        with open(os.path.join(os.getcwd(), 'src', 'vocabtrainer', 'english.txt'), 'r') as fh:
            content = fh.readlines()
        for line in content:
            if line.startswith('#'):
                continue
            eng, ger = line.split(';')
            eng = eng.strip(' \n\t')
            ger = ger.strip(' \n\t')
            if eng not in self.vocab_eng.keys():
                self.vocab_eng[eng] = ger
        with open(os.path.join(os.getcwd(), 'src', 'vocabtrainer', 'latein.txt'), 'r') as fh:
            content = fh.readlines()
        for line in content:
            lat, ger = line.split(';')
            lat = lat.strip(' \n\t')
            ger = ger.strip(' \n\t')
            if lat not in self.vocab_lat.keys():
                self.vocab_lat[lat] = ger

    def start_up(self):
        self.window = sg.Window('Vokabeltrainer', self.layout)

        while True:  # Event Loop
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == '-CHECK-':
                self.cb_check(values)
            if event in ['-ENG-', '-LAT-']:
                if values['-ENG-'] == True:
                    self.cb_eng(values)
                    
                if values['-ENG-'] == False:
                    self.cb_lat(values)

        self.window.close()

    def cb_check(self, values):
        if values['-IN-'] == self.translation or values['-IN-'].lower() in self.translation.lower() and values['-IN-'] != '':
            self.cnter_correct += 1
            self.window['-CORRECT-'].update(self.cnter_correct)
            self.window['-IN-'].update('')
        elif values['-IN-'] == '':
            self.cnter_incorrect += 1
            self.window['-INCORRECT-'].update(self.cnter_incorrect)
        else:
            self.cnter_incorrect += 1
            self.window['-INCORRECT-'].update(self.cnter_incorrect)
        if values['-ENG-'] == True:
            self.shown_word, self.translation = random.choice(list(self.vocab_eng.items()))
        if values['-LAT-'] == True:
            self.shown_word, self.translation = random.choice(list(self.vocab_lat.items()))
        self.window['-OUTPUT-'].update(self.shown_word)

    def cb_eng(self, values):
        self.shown_word, self.translation = random.choice(list(self.vocab_eng.items()))
        self.window['-OUTPUT-'].update(self.shown_word)
        self.window['-IN-'].update('')

    def cb_lat(self, values):
        self.shown_word, self.translation = random.choice(list(self.vocab_lat.items()))
        self.window['-OUTPUT-'].update(self.shown_word)
        self.window['-IN-'].update('')

if __name__ == '__main__':
    gui = gui()
    gui.start_up()