# Konkrurentsiamet
Minu lahendus Konkurentsiameti andmeinseneri praktika kodutööle.

# Kuidas kasutada
Esmaslt tuleks allalaadida vajalikud teegid, olles root folderis kasutada käsku pip install -r requirements.txt

Käivitada main.py, saadakse PNG formaadis pilt graafikust, mis kujutab elektrihindu tunnitäpsusega, CSV fail hindadest tunni täpsusega, ning CSV fail erinevatest näitajatest ka. keskmine hind.

# Lahenduse kirjeldus
Lahendus algab get_data.py failist, kus otsitakse allalaetud HTML failist üles õige tabel, ning loetakse seal olevaid andmeid. Selleks kasutasin BeautifulSoap teeki.

Järgnevalt failis data_processing.py pannakse saadud andmed "dataframe"-i kasutades pandas teeki.

Viimaks failis visualize.py kantakse "dataframe"-i andmed graafikule, mis saadakse PNG formaadis, ning lisaks saadakse kaks CSV faili, kus ühes elektrihinnad tundide täpsusega, ning teises erinevad näitajad kogutud andmete alusel.
