def main():
    album = {
        "Artist name": "Sandra",
        "Album name": "Paintings In Yellow",
        "Label": "Virgin – 260 518-222, Virgin – CDV 2636",
        "Format": "CD, Album",
        "Country": "Germany",
        "Released": 1990,
        "Genre": "Electronic",
        "Style": "Synth-pop",
        "Barcode and other identifiers": "",
        "Barcode (Printed)": "3 268442 605185",
        "Barcode (Scanned)": "3268442605185",
        "Label Code": "LC 3098",
        "Rights Society": "GEMA / STEMRA / BIEM",
        "Matrix / Runout": "SONOPRESS 260518 B",
        "Price Code (France)": "PM527",
        "Tracks": [
            ("Hiroshima", 410),
            ("(Life May Be) A Big Insanity", 269),
            ("Johnny Wanna Live", 266),
            ("Lovelight In Your Eyes", 327),
            ("One More Night", 246),
            ("The Skin I'm In", 220),
            ("Paintings In Yellow", 350),
            ("The Journey (Cold Out Here, I'm Alive, Paintings, Come Alive, The End)", 447),
            ("Hiroshima (Extended Club Mix)", 404)
        ]
    }
    while True:
        print('''\n\n
                    --- CD DASHBOARD ---\n
                exit = Leave the system.
                album = Prints Album info.
                tracklist = Prints Tracklist info.
                edit album = Album edit menu.
                edit tracklist = Tracklist edit menu.
                duration = Prints total duration of this album.
              \n\n''')
        choice = input("Select the menu item you want: ")
        if choice.startswith("exit"):
            quit
        elif choice.startswith("edit album"):
            edit_album(album)
        elif choice.startswith("edit tracklist"):
            edit_tracklist(album)
        elif choice.startswith("album"):
            print_album(album)
        elif choice.startswith("tracklist"):
            print_tracklist(album)
        elif choice.startswith("duration"):
            total_duration(album)
        else:
            print("Incorrect command, please try again!")


def print_album(album):
    for key, value in album.items():
        printable_key = key + ":"
        print(f"{printable_key:20} {value}")
    print("\n")


def print_tracklist(album):
    for index, track_info in enumerate(album["Tracks"], start=1):
        track_name, track_duration = track_info
        print(f"{index:02d} - {track_name:<70}\t{format_duration(track_duration)}")


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
                print("Invalid track number. Please choose a valid track.")
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
