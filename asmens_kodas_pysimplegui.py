import PySimpleGUI as sg

def check_asmens_kodas(asmens_kodas):
    if not asmens_kodas.isnumeric() or len(asmens_kodas) != 11:
        return 'Neteisingas: turi būti 11 skaitmenų skaičius.'

    menuo = int(asmens_kodas[3:5])
    if menuo < 1 or menuo > 12:
        return 'Neteisingas: mėnuo gimimo datoje negali būti didesnis už 12 arba lygus 0.'

    diena = int(asmens_kodas[5:7])
    if diena < 1 or diena > 31:
        return 'Neteisingas: diena gimimo datoje negali būti didesnė už 31 arba lygus 0.'

    # Paskutinio skaičiaus tikrinimas
    daugikliai = '1234567891'
    kiti_daugikliai = '3456789123'
    kontrolinis = 0

    for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
        kontrolinis += int(skaitmuo) * int(daugikliai[daugiklio_nr])

    if kontrolinis % 11 == 10:
        kontrolinis = 0
        for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
            kontrolinis += int(skaitmuo) * int(kiti_daugikliai[daugiklio_nr])

    tikrinamas = kontrolinis % 11
    if tikrinamas == 10:
        tikrinamas = 0

    paskutinis = int(asmens_kodas[10])
    if paskutinis != tikrinamas:
        return 'Neteisingas: paskutinis skaičius klaidingas.'

    return 'TEISINGAS'

while True:
    layout = [
        [sg.Text('Įveskite asmens kodą:')],
        [sg.InputText(key='-ASMENS_KODAS-')],
        [sg.Button('Patikrinti'), sg.Button('Išeiti')],
        [sg.Output(size=(50, 10))]
    ]

    window = sg.Window('Asmens kodo tikrinimas', layout)

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Išeiti':
        print('viso gero :)')
        break

    asmens_kodas = values['-ASMENS_KODAS-']
    result = check_asmens_kodas(asmens_kodas)
    print(result)

    window.close()