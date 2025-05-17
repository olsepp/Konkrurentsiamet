# Konkrurentsiamet
Minu lahendus Konkurentsiameti andmeinseneri praktika kodutööle.

# Kuidas kasutada
Käivitades main.py saadakse jpg formaadis pilt graafikust, mis kujutab elektrihindu tunnitäpsusega, CSV faili hindadest tunni täpsusega, ning CSV faili erinevatest näitajatest ka. keskmine hind.

# Lahenduse kirjeldus
Lahendus algab get_data.py failist, kus otsitakse allalaetud HTML failist üles õige tabel, ning loetakse seal olevaid andmeid. Selleks kasutasin BeautifulSoap teeki.

Järgnevalt failis data_processing.py pannakse saadud andmed "dataframe"-i kasutades pandas teeki.

Viimaks failis visualize.py kantakse "dataframe"-i andmed graafikule, mis saadakse JPG formaadis, ning lisaks saadakse kaks CSV faili, kus ühes elektrihinnad tundide täpsusega, ning teine erinevatest näitajatest kogutud andmete alusel.
