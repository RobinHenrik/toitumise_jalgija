import time
from profiilid_sonastikku import profiilid_sõnastikku
from profiilid import profiilid
import andmebaasi_funktsioonid
import toidukorrad


profiili_andmed = profiilid()
toidu_andmebaas = andmebaasi_funktsioonid.toidud_sõnastikku()

nimi = profiili_andmed['nimi']
toidukorrad.toidukorra_lisamine(nimi, toidu_andmebaas)

