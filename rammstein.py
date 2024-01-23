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

    while True:
        print('''
                    --- CD DASHBOARD ---\n
                0 = Leave the system.
                1 = Add a new CD to collection.
                2 = Remove CD from collection.
                3 = View my collection.
              
                
                album = Prints Album info.
                tracklist = Prints Tracklist info.
                edit album = Album edit menu.
                edit tracklist = Tracklist edit menu.
                duration = Prints total duration of this album.

              \n\n''')
                
        choice = input("Select the menu item you want: ")
        if choice.startswith("0"):
            quit
        elif choice.startswith("edit album"):
            edit_album(cd_info)
        elif choice.startswith("edit tracklist"):
            edit_tracklist(cd_info)
        elif choice.startswith("album"):
            print_album(cd_info)
        elif choice.startswith("tracklist"):
            print_tracklist(cd_info)
        elif choice.startswith("duration"):
            total_duration(cd_info)
        else:
            print("Bad choice, try again")


def print_album(cd_info):
    for key, value in cd_info.items():
        print(f"{key} - {value}")


def print_tracklist(cd_info):
    print("---TRACKLIST INFO---")
    for index, track_info in enumerate(cd_info["Tracks"], start=1):
        track_name, track_duration = track_info
        print(f"{index}. {track_name} - {format_duration(track_duration)}")


def edit_album(album):
    while True:
        print("""
            ----Album edit menu----
            1. Edit artist name.
            2. Edit album name.
            3. Edit album year.
            4. Tracklist edit menu.
            0. Back
            album = Prints Album info.
            exit = Exits program.
            """)
        choice = input("Your choice: ")
        if choice.startswith("0"):
            break
        elif choice.startswith("exit"):
            quit()
        elif choice.startswith("album"):
            print_album(album)
        elif choice.startswith("1"):
            new_artist_name = input("Input new artist name: ")
            album["Artist"] = new_artist_name
        elif choice.startswith("2"):
            new_album_name = input("Input new album name: ")
            album["Album name"] = new_album_name
        elif choice.startswith("3"):
            new_album_year = int(input("Input new album year: "))
            album["Year"] = new_album_year
        elif choice.startswith("4"):
            edit_tracklist(album)
        else:
            print("Wrong choice")


def edit_tracklist(album):
    while True:
        print("""
            ----Tracklist edit menu----
            0. Back
            1. Edit track name.
            2. Edit track duration.
            3. Add new track.
            4. Album edit menu.
            5. Remove track.
            exit = Exits program
            tracklist = Prints Tracklist info.
            album = Prints Album info.
            """)
        choice = input("Your choice: ")
        if choice.startswith("0"):
            break
        elif choice.startswith("exit"):
            quit()
        elif choice.startswith("tracklist"):
            print_tracklist(album)
        elif choice.startswith("album"):
            print_album(album)           
        elif choice.startswith("1"):
            print_tracklist(album)
            chose_track = int(input("Chose track number to edit: "))
            new_track_name = input("Input new track name: ")
            album["Tracks"][chose_track-1] = (new_track_name, album["Tracks"][chose_track-1][1])
        elif choice.startswith("2"):
            print_tracklist(album)
            chose_track = int(input("Chose track number to edit: "))
            new_track_duration = input("Input new duration (MM:SS): ")
            album["Tracks"][chose_track-1] = (album["Tracks"][chose_track-1][0], parse_duration(new_track_duration))
        elif choice.startswith("3"):
            print_tracklist(album)
            track_info = input("Input new track name, duration (MM:SS): ") 
            album["Tracks"].append(parse_track_info(track_info))
        elif choice.startswith("4"):
            edit_album(album)
        elif choice.startswith("5"):
            print_tracklist(album)
            del_choice = int(input("Choose track to delete: "))
            if 1 <= del_choice <= len(album["Tracks"]):
                del album["Tracks"][del_choice - 1]
                break
            else:
                print("Invalid track number. Please choose a valid track next time.")
                break
        else:
            print("Wrong choice")

def format_duration(seconds):
    seconds_left = seconds % 60
    minutes = seconds // 60
    return f"{minutes:02}:{seconds_left:02}"

def parse_duration(track_duration):
    if isinstance(track_duration, str):
        parts = track_duration.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])
        return minutes * 60 + seconds
    elif isinstance(track_duration, int):
        return track_duration
    else:
        raise ValueError("Invalid track duration format")


def parse_track_info(track_info):
    parts = track_info.split(", ")
    track_name = parts[0]
    duration_parts = parts[1].split(":")
    minutes = int(duration_parts[0])
    seconds = int(duration_parts[1])
    track_duration = minutes * 60 + seconds
    return track_name, track_duration


def total_duration(album):
    album_duration = 0
    for track_info in album["Tracks"]:
        album_duration += track_info[1]
    print("Total album duration in seconds: ", album_duration)
    print("Totel album duration in (MM:SS) format:", format_duration(album_duration))


if __name__ == "__main__":
    main()

""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""
