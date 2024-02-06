import PySimpleGUI as sg
import sqlite3
import pycountry


connection = sqlite3.connect('visa.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        firstname text,
        lastname text,
        gender text,
        maritalstatus text,
        dateofbirth text,
        country text,
        address text,
        phone integer,
        passportnumber text,
        passporttype text,
        expirydate text
        )""")

connection.commit()
cursor.close()
connection.close()

sg.theme('LightGreen8')
sg.set_options(font=('SegoeUILight 11'))
country_list = [country.name for country in pycountry.countries]

layout = [
    [sg.T('Registration form for VISA \n \n')],

    [sg.T('Personal Information: \n')],

    [sg.T('Select Photo'),
     sg.Push(),
     sg.FileBrowse(size=(10, 1),
                   key='PHOTO')],

    [sg.T('First Name'),
     sg.Push(),
     sg.I(size=(30,3),
          key='FIRSTNAME')],
    
    [sg.T('Last Name'),
     sg.Push(),
     sg.I(size=(30,3),
          key='LASTNAME')],

    [sg.T('Gender'),
     sg.Push(),
     sg.Combo(size=(29, 3),
              values=['Male','Female'],
              key='GENDER')],

    [sg.T('Marital status'),
     sg.Push(),
     sg.Combo(size=(29, 5),
              values=['Single','Married', 'Divorced', 'Widowed'],
              key='MARITALSTATUS')],

    [sg.T('\n \n \n Date and Place of Birth: \n')],

    [sg.T('Date of Birth'),
     sg.Push(),
     sg.CalendarButton(size=(14, 1),
                       button_text='Choose A Date',
                       format='%d-%m-%Y',
                       no_titlebar=True,
                       close_when_date_chosen=True,
                       target='DATEOFBIRTH',
                       default_date_m_d_y=(1, 1, 1970)),
                       sg.InputText(size=(30, 3),
                                    key='DATEOFBIRTH')],
    
    [sg.T('Country'),
     sg.Push(),
     sg.Combo(size=(29, 10),
              values=country_list,
               key='COUNTRY')],

    [sg.T('Address'),
     sg.Push(),
     sg.ML(size=(29, 3),
           key='ADDRESS')],

    [sg.T('Phone Contact'),
     sg.Push(),
     sg.I(size=(30,3),
          key='PHONE')],

    [sg.T('\n \n \n Passport Information: \n')],

    [sg.T('Passport Number'),
     sg.Push(),
     sg.I(size=(30,3),
          key='PASSPORTNUMBER')],

    [sg.T('Passport Type'),
     sg.Push(),
     sg.Combo(size=(29, 7),
              values=['Ordinary',
                      'Diplomatic',
                      'Service',
                      'Special',
                      'International Organization',
                      'Travel Document'],
              key='PASSPORTTYPE')],

    [sg.T('Expiry Date'),
     sg.Push(),
     sg.CalendarButton(size=(14, 1),
                       button_text='Choose A Date',
                       format='%d-%m-%Y',
                       no_titlebar=True,
                       close_when_date_chosen=True,
                       target='EXPIRYDATE',
                       default_date_m_d_y=(1, 1, 2050)),
                       sg.InputText(size=(30, 3),
                                    key='EXPIRYDATE')],    

    [sg.Text('\n')],

    [sg.Button('Submit', expand_x=True),
     sg.Button('Clear', expand_x=True),
     sg.Button('Show VISA', expand_x=True),
     sg.Button('Exit', expand_x=True)]
]

window = sg.Window('Tanzania eVisa Application System', layout)

def retrieve_user_records():
    results = []
    connection = sqlite3.connect('visa.db')
    cursor = connection.cursor()
    query = "SELECT firstname, lastname, gender, maritalstatus, dateofbirth, country, address, phone, passportnumber, passporttype, expirydate from users"
    cursor.execute(query)
    for row in cursor:
        results.append(list(row))
    return results

def get_user_records():
    client_records=retrieve_user_records()
    return client_records

def create_records():
    client_records_array = get_user_records()
    headings = ['FIRST NAME', 'LAST NAME', 'GENDER', 'MARITAL STATUS', 'DATE OF BIRTH', 'COUNTRY','ADDRESS', 'PHONE NUMBER', 'PASSPORT NUMBER', 'PASSPORT TYPE', 'EXPIRY DATE']

    layout_for_display = [
        [sg.Table(values = client_records_array,
                  headings = headings,
                  max_col_width = 50,
                  auto_size_columns = True,
                  display_row_numbers = True,
                  justification = 'justify',
                  num_rows = 5,
                  key = 'USERTABLE',
                  row_height = 100,
                  enable_events = True,
                  tooltip = 'all users results'
                  )],
    ]
    windr = sg.Window('Summary results', layout_for_display, modal=True)

    while True:
        event, values = windr.read()
        if event == sg.WIN_CLOSED:
            break

def clear_inputs():
    for key in values:
        window['FIRSTNAME'].update('')
        window['LASTNAME'].update('')
        window['GENDER'].update('')
        window['MARITALSTATUS'].update('')
        window['DATEOFBIRTH'].update('')
        window['COUNTRY'].update('')
        window['ADDRESS'].update('')
        window['PHONE'].update('')
        window['PASSPORTNUMBER'].update('')
        window['PASSPORTTYPE'].update('')
        window['EXPIRYDATE'].update('')
    return None
def save_data_to_database():
    connection = sqlite3.connect('visa.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (:firstname, :lastname, :gender, :maritalstatus, :dateofbirth, :country, :address, :phone, :passportnumber, :passporttype, :expirydate)",
              {
                'firstname': values['FIRSTNAME'],
                'lastname': values['LASTNAME'],
                'gender': values['GENDER'],
                'maritalstatus': values['MARITALSTATUS'],
                'dateofbirth': values['DATEOFBIRTH'],
                'country': values['COUNTRY'],
                'address': values['ADDRESS'],
                'phone': values['PHONE'],
                'passportnumber': values['PASSPORTNUMBER'],
                'passporttype': values['PASSPORTTYPE'],
                'expirydate': values['EXPIRYDATE']

              })

    connection.commit()
    cursor.close()
    connection.close()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Clear':
        clear_inputs()
    if event == 'Show VISA':
        create_records()
    if event == 'Submit':
        firstname = values['FIRSTNAME']
        if firstname == '':
            sg.PopupError('Missing first name!', 'Please insert first name before you continue!')
        lastname = values['LASTNAME']
        if lastname == '':
            sg.PopupError('Missing last name!', 'Please insert last name before you continue!')
        gender = values['GENDER']
        if gender == '':
            sg.PopupError('Missing gender!', 'Please insert gender before you continue!')
        maritalstatus = values['MARITALSTATUS']
        if maritalstatus == '':
            sg.PopupError('Missing marital status!', 'Please insert marital status before you continue!')
        dateofbirth = values['DATEOFBIRTH']
        if dateofbirth == '':
            sg.PopupError('Missing Date of Birth!', 'Please insert date of birth before you continue!')
        country = values['COUNTRY']
        if country == '':
            sg.PopupError('Missing country!', 'Please insert country before you continue!')
        address = values['ADDRESS']
        if address == '':
            sg.PopupError('Missing address!', 'Please insert address before you continue!')
        phone = values['PHONE']
        if phone == '':
            sg.PopupError('Missing phone contact!', 'Please insert phone contact before you continue!')
        passportnumber = values['PASSPORTNUMBER']
        if passportnumber == '':
            sg.PopupError('Missing passport number!', 'Please insert passport number before you continue!')
        passporttype = values['PASSPORTTYPE']
        if passporttype == '':
            sg.PopupError('Missing passport type!', 'Please insert passport type before you continue!')
        expirydate = values['EXPIRYDATE']
        if expirydate == '':
            sg.PopupError('Missing passport expiry date!', 'Please insert passport expiry date before you continue!')
        else:
            try:
                summary_list = "The following information has been added to the database: \n \n"
                summary_list += "Personal Information: \n"
                summary_list += f"\nFirst Name:\n{values['FIRSTNAME']}"
                summary_list += f"\n\nLast Name:\n{values['LASTNAME']}"
                summary_list += f"\n\nGender:\n{values['GENDER']}"
                summary_list += f"\n\nMarital status:\n{values['MARITALSTATUS']}"
                summary_list += "\n\n\nDate and Place of Birth: \n"
                summary_list += f"\nDate of Birth:\n{values['DATEOFBIRTH']}"
                summary_list += f"\n\nCountry:\n{values['COUNTRY']}"
                summary_list += f"\n\nAddress:\n{values['ADDRESS']}"
                summary_list += f"\n\nPhone Contact:\n{values['PHONE']}"
                summary_list += "\n\n\nPassport Information: \n"
                summary_list += f"\nPassport Number\n{values['PASSPORTNUMBER']}"
                summary_list += f"\n\nPassport Type\n{values['PASSPORTTYPE']}"
                summary_list += f"\n\nExpiry Date\n{values['EXPIRYDATE']}"
                choice = sg.PopupOKCancel(summary_list, '\nPlease confirm the entry with OK, or press CANCEL to return to editing')
                if choice == 'OK':
                    clear_inputs()
                    save_data_to_database()
                    sg.PopupQuick('Saved to database!')
                else:
                    sg.PopupOK('Return to edit entry')
            except:
                sg.popup('Some error, kindly report to the admin team')

window.close()
