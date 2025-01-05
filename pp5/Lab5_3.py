kwota_poczatkowa = 46567.
kwota_po_3_roku = kwota_poczatkowa
kwota_po_3_roku *= 1.075**3
kwota_po_3_roku = str(round(kwota_po_3_roku, 2))
kwota_po_3_roku = kwota_po_3_roku.replace(".", ",")

print("Kwota 46567,00 na trzyletniej lokacie ze stałym rocznym oprocentowaniem w wysokości 7,5% to:", kwota_po_3_roku)