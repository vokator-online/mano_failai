def main():
    print("\n")
    cd_info = {
        'Artist': 'Rammstein',
        'Album': 'Made In Germany 1995-2011',
        'Label': 'Universal Music Group – 0602527864273',
        'Format': ['2 x CD', 'Compilation', 'Reissue', 'Remastered', 'Kruspe Cover'],
        'Country': 'Europe',
        'Released': '2011',
        'Genre': ['Electronic', 'Rock'],
        'Style': 'Industrial'
    }

    for key, value in cd_info.items():
        printable_key = key + ":"
        if type(value) == list:
            value = ', '.join(value)
        print(f"{printable_key:10} {value}")
    print("\n")

    barcode_and_other_identifiers = {
        'Barcode (Text)': '0 602527 864273',
        'Barcode (Scanned)': '0602527864273',
        'Label Code': 'LC 14513',
        'Rights Society': 'BIEM/SDRM',
        'Matrix / Runout (CD1)': '[4x Universal logo] arvato 56335125/00602527864280 21',
        'Mastering SID Code (CD1)': 'IFPI LP47',
        'Mould SID Code (CD1)': 'IFPI 0772',
        'Matrix / Runout (CD2)': '[4x Universal logo] U 56341561/00602527864297 21',
        'Mastering SID Code (CD2)': 'IFPI LQ57',
        'Mould SID Code (CD2)': 'IFPI 0792'
    }

    for key, value in barcode_and_other_identifiers.items():
        printable_key = key + ":"
        if type(value) == list:
            value = ', '.join(value)
        print(f"{printable_key:25} {value}")
    print("\n")

    print('CD 1 (Compilation):\n')
    cd1_songs = [
        {"title": "Engel (Voice [Female Voice] – Bobo)", "duration": "04:23"},
        {"title": "Links 2 3 4", "duration": "03:40"},
        {"title": "Keine Lust", "duration": "03:42"},
        {"title": "Mein Teil", "duration": "04:38"},
        {"title": "Du Hast", "duration": "03:54"},
        {"title": "Du Riechst So Gut", "duration": "04:32"},
        {"title": "Ich Will", "duration": "03:37"},
        {"title": "Mein Herz Brennt", "duration": "04:40"},
        {"title": "Mutter", "duration": "04:28"},
        {"title": "Pussy", "duration": "03:58"},
        {"title": "Rosenrot", "duration": "03:52"},
        {"title": "Haifisch", "duration": "03:42"},
        {"title": "Amerika", "duration": "03:47"},
        {"title": "Sonne", "duration": "04:05"},
        {"title": "Ohne Dich", "duration": "04:30"},
        {"title": "Mein Land", "duration": "03:53"}
    ]

    for index, song in enumerate(cd1_songs, start=1):
        title = f"{song['title']:<50}"
        duration = f"{song['duration']:>5}"
        print(f"{index:02d} - {title}\t{duration}")
    print("\n")

    print('CD 2 (Remixes):\n')
    cd2_songs = [
        {"title": "Du Riechst So Gut '98 (Rmx By Faith No More)", "duration": "01:58"},
        {"title": "Du Hast (Rmx By Jacob Hellner)", "duration": "06:42"},
        {"title": "Stripped (Rmx By Johan Edlund (Tiamat))", "duration": "04:22"},
        {"title": "Sonne (Rmx By Clawfinger)", "duration": "04:09"},
        {"title": "Links 2 3 4 (Rmx By Westbam)", "duration": "03:40"},
        {"title": "Mutter (Rmx By Sono)", "duration": "07:21"},
        {"title": "Feuer Frei! (Rmx By Junkie XL)", "duration": "04:10"},
        {"title": "Mein Teil (Rmx By Pet Shop Boys)", "duration": "04:04"},
        {"title": "Amerika (Rmx By Olsen Involtini)", "duration": "03:15"},
        {"title": "Ohne Dich (Rmx By Laibach)", "duration": "03:58"},
        {"title": "Keine Lust (Rmx By Black Strobe)", "duration": "07:07"},
        {"title": "Benzin (Rmx By Meshuggah)", "duration": "05:05"},
        {"title": "Rosenrot (Rmx By Northern Lite)", "duration": "04:46"},
        {"title": "Pussy (Rmx By Scooter)", "duration": "04:53"},
        {"title": "Rammlied (Rmx By Devin Townsend)", "duration": "05:06"},
        {"title": "Ich Tu Dir Weh (Rmx By Fukkk Offf)", "duration": "06:08"},
        {"title": "Haifisch (Rmx By Hurts)", "duration": "03:45"}
    ]

    for index, song in enumerate(cd2_songs, start=1):
        title = f"{song['title']:<50}"
        duration = f"{song['duration']:>5}"
        print(f"{index:02d} - {title}\t{duration}")
    print("\n")

    while True:                                                             # Work with the system
        print('''\n\n
                    --- CD DASHBOARD ---\n
                0 = Leave the system.
                1 = Add a new CD to collection.
                2 = Remove CD from collection.
                3 = View my collection.
              \n\n''')
        choice = input("Select the menu item you want: ")
        if choice == "0":
            break
        elif choice == "1":
            artist = input("Artist: ")
            title = input('Title: ')
            data = input('Released: ')
            add_cd(data, artist, title)
        elif choice == "2":
            artist = input("Artist: ")
            title = input('Title: ')
            data = input('Released: ')
            remove_cd(data, artist, title)
        elif choice == "3":
            list_cds()
        else:
            print("Incorrect command, please try again!")

cd_information = []                                                            # Information about the Compact Disc

def add_cd(data, artist, album):
    cd_initials = {'data': data, 'artist': artist, 'album': album }
    cd_information.append(cd_initials)
    print(f"\nCD\t{data} {artist} - {album}\tadded to collection.")

def remove_cd(data, artist, album):
    for cd_initials in cd_information:
        if cd_initials['artist'] == artist and cd_initials['album'] == album:
            cd_information.remove(cd_initials)
            print(f"\nCD\t{data} {artist} - {album}\tremoved from collection.")
            return
    print(f"\nCD\t{artist} - {album}\tnot found in collection.")

def list_cds():
    print('CDs in the collection:')
    for index, cd_initials in enumerate(cd_information, start=1):
        print(f'\n{index}. {cd_initials["data"]} {cd_initials["artist"]} - {cd_initials["album"]}')


if __name__ == "__main__":
    main()