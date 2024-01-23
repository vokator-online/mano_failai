import PySimpleGUI as sg

def main():
    # Sukurti grafinę sąsają
    layout = [
        [sg.Text('Registracija vizitui pas daktarą AI, SKAUDA!')],
        [sg.Text('Vardas', size=(15, 1)), sg.InputText(key='vardas')],
        [sg.Text('Pavardė', size=(15, 1)), sg.InputText(key='pavardė')],
        [sg.Text('Gimimo metai', size=(15, 1)), sg.InputText(key='gimimo metai')],
        [sg.Button('Patvirtinti'), sg.Button('Išeiti')]
    ]

    # Sukurti langą iš sudaryto sąsajos
    window = sg.Window('SK ZbygMed Brambai Enclosure', layout)

    # Programos pagrindinė ciklo dalis
    while True:
        event, values = window.read()

        # Patikrinti, ar langas yra gyvas
        if event == sg.WIN_CLOSED or event == 'Išeiti':
            break

        # Reakcija į mygtuko paspaudimą
        if event == 'Patvirtinti':
            vardas = values['vardas'].capitalize()
            pavardė = values['pavardė'].capitalize()

            try:
                gimimo_metai = int(values['gimimo metai'])
            except ValueError:
                sg.popup_error('Įveskite skaičių gimimo metais!')
                continue  # Grąžiname programą į ciklo pradžią

            sg.popup(f'Sveiki, {vardas} {pavardė}!\nJūs sėkmingai užsiregistravote pas daktarą AI, SKAUDA!')

    # Uždaryti langą ir išeiti iš programos
    window.close()

if __name__ == '__main__':
    main()