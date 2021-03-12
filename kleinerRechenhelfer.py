# -*- coding: utf-8 -*-
import math

def truncate(number, decimals=3):
    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

try:
    gesamtbetrag_brutto = float(input("Gesamtbetrag brutto: "))
except ValueError:
    gesamtbetrag_brutto = 0

try:
    gesamtbetrag_netto = float(input("Gesamtbetrag netto: "))    
except ValueError:    
    gesamtbetrag_netto = 0

try:
    prozent_1 = float(input("Erster Prozentbetrag: "))
except ValueError:
    prozent_1 = 0

try:
    prozent_2 = float(input("Zweiter Prozentbetrag: "))
except ValueError:
    prozent_2 = 0
    
try:
    prozent_3 = float(input("Dritter Prozentbetrag: "))
except ValueError:
    prozent_3 = 0

try:
    prozent_4 = float(input("Vierter Prozentbetrag: "))    
except ValueError:
    prozent_4 = 0
    
try:
    monate = int(input("Anzahl der Monate: "))
except ValueError:
    monate = 0


# Erster Prozentbetrag wird ausgerechnet
if prozent_1 != 0:
    if gesamtbetrag_brutto > 0:
        eins_brutto = truncate((gesamtbetrag_brutto / 100) * prozent_1)
        print(f"\nErster Wert ({prozent_1}% BRUTTO): {eins_brutto}")
        if monate > 1:
            monat_brutto_1 = truncate(eins_brutto / monate)
            print(f"Ein Monat BRUTTO: {monat_brutto_1} | In 12 Monaten: {truncate(12 * monat_brutto_1)}")

    if gesamtbetrag_netto > 0:
        eins_netto = truncate((gesamtbetrag_netto / 100) * prozent_1)
        print(f"\nErster Wert ({prozent_1}% NETTO): {eins_netto}")
        if monate > 1:
            monat_netto_1 = truncate(eins_netto / monate)
            print(f"Ein Monat NETTO: {monat_netto_1} | In 12 Monaten: {truncate(12 * monat_netto_1)}")


# Zweiter Prozentbetrag wird ausgerechnet
if prozent_2 != 0:
    if gesamtbetrag_brutto > 0:
        zwei_brutto = truncate((gesamtbetrag_brutto / 100) * prozent_2)
        print(f"\nZweiter Wert ({prozent_2}% BRUTTO): {zwei_brutto}")
        if monate > 1:
            monat_brutto_2 = truncate(zwei_brutto / monate)
            print(f"Ein Monat BRUTTO: {monat_brutto_2} | In 12 Monaten: {truncate(12 * monat_brutto_2)}")

    if gesamtbetrag_netto > 0:
        zwei_netto = truncate((gesamtbetrag_netto / 100) * prozent_2)
        print(f"\nZweiter Wert ({prozent_2}% NETTO): {zwei_netto}")
        if monate > 1:
            monat_netto_2 = truncate(zwei_netto / monate)
            print(f"Ein Monat NETTO: {monat_netto_2} | In 12 Monaten: {truncate(12 * monat_netto_2)}")


# Dritter Prozentbetrag wird ausgerechnet
if prozent_3 != 0:
    if gesamtbetrag_brutto > 0:
        drei_brutto = truncate((gesamtbetrag_brutto / 100) * prozent_3)
        print(f"\nDritter Wert ({prozent_3}% BRUTTO): {drei_brutto}")
        if monate > 1:
            monat_brutto_3 = truncate(drei_brutto / monate)
            print(f"Ein Monat BRUTTO: {monat_brutto_3} | In 12 Monaten: {truncate(12 * monat_brutto_3)}")

    if gesamtbetrag_netto > 0:
        drei_netto = truncate((gesamtbetrag_netto / 100) * prozent_3)
        print(f"\nDritter Wert ({prozent_3}% NETTO): {drei_netto}")
        if monate > 1:
            monat_netto_3 = truncate(drei_netto / monate)
            print(f"Ein Monat NETTO: {monat_netto_3} | In 12 Monaten: {truncate(12 * monat_netto_3)}")
 

# Vierter Prozentbetrag wird ausgerechnet
if prozent_4 != 0:
    if gesamtbetrag_brutto > 0:
        vier_brutto = truncate((gesamtbetrag_brutto / 100) * prozent_4)
        print(f"\nVierter Wert ({prozent_4}% BRUTTO): {vier_brutto}")
        if monate > 1:
            monat_brutto_4 = truncate(vier_brutto / monate)
            print(f"Ein Monat BRUTTO: {monat_brutto_4} | In 12 Monaten: {truncate(12 * monat_brutto_4)}")
    
    if gesamtbetrag_netto > 0:
        vier_netto = truncate((gesamtbetrag_netto / 100) * prozent_4)
        print(f"\nVierter Wert ({prozent_4}% NETTO): {vier_netto}")
        if monate > 1:   
            monat_netto_4 = truncate(vier_netto / monate)
            print(f"Ein Monat NETTO: {monat_netto_4} | In 12 Monaten: {truncate(12 * monat_netto_4)}")


# print(eins_brutto + zwei_brutto + drei_brutto)
