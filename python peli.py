def aloita_peli():
    print("Tervetuloa Piparimetsän valtakuntaan!")
    nimi = input("Mikä on nimesi, seikkailija? ")
    print(f"Tervetuloa, {nimi}! Olet valmis aloittamaan seikkailusi kohti piparimetsää.")
    print("\n")
    
    alku_tarina()

def alku_tarina():
    print("Olet metsässä ja näet kaksi polkua edessäsi.")
    valinta = input("Haluatko kävellä vasemmalle polulle (1) vai oikealle polulle (2)? ")

    if valinta == "1":
        vasen_polku()
    elif valinta == "2":
        oikea_polku()
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        alku_tarina()

def vasen_polku():
    print("\nKävelit vasemmalle polulle ja saavuit piparkakkutalon eteen.")
    valinta = input("Haluatko avata oven (1) vai kiertää talon ympäri (2)? ")

    if valinta == "1":
        print("\nOvi on lukossa. Sinun täytyy löytää avain.")
        avain = input("Näet avaimen lyhdyn sisällä. Ota avain (1) vai jätä se sinne (2)? ")

        if avain == "1":
            print("\nOlet ottanut avaimen ja avannut oven. Sisällä on salainen resepti!")
            print("Onneksi olkoon, löysit salaisen reseptin ja nyt voit tehdä maailman parhaita pipareita!")
            peli_loppu("voitto")
        else:
            print("\nEt ottanut avainta ja jäädyt talon eteen.")
            peli_loppu("häviö")

    elif valinta == "2":
        print("\nTalon takana on jäinen loiva kallio, jota voit laskea alas ja löytää joen.")
        print("Olet löytänyt uuden polun ja jatkat matkaasi.")
        peli_loppu("aikalisä")

    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        vasen_polku()

def oikea_polku():
    print("\nKävelit oikealle polulle ja kohtaat piparimiehen!")
    valinta = input("Haluatko taistella piparimiehen kanssa (1) vai juosta pakoon (2)? ")

    if valinta == "1":
        print("\nPiparimies on liian vahva ja et onnistu nujertamaan häntä.")
        peli_loppu("häviö")
    elif valinta == "2":
        print("\nPakenit piparimiestä ja löysit turvapaikan lähimetsän puun takaa.")
        peli_loppu("aikalisä")
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        oikea_polku()

def peli_loppu(tulos):
    if tulos == "voitto":
        print("\nVoitit pelin! Onnittelut, seikkailija!")
    elif tulos == "häviö":
        print("\nPeli päättyi. Yritä uudelleen.")
    elif tulos == "aikalisä":
        print("\nPeli ei päättynyt, mutta joudut jatkamaan matkaa.")
    else:
        print("\nPeli päättyi tuntemattomasta syystä.")
    
    uudelleen = input("\nHaluatko pelata uudestaan? (kyllä/ei) ")
    if uudelleen.lower() == "kyllä":
        aloita_peli()
    else:
        print("Kiitos pelaamisesta!")

# Aloitetaan peli
aloita_peli()
