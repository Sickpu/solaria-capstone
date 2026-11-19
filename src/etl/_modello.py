"""
terna.py

Cosa fa: legge il file Excel dei consumi elettrici per provincia
scaricato dal sito di Terna, lo pulisce e salva una tabella
con una riga per provincia.

File di partenza: data/raw/terna/consumi_2023.xlsx
    (scaricato a mano dal sito Terna il 20/11/2026)
File prodotto:    data/interim/terna.parquet
Colonne prodotte: cod_prov, consumi_totali_mwh, consumi_domestici_mwh
Autore: Martina
"""

import pandas as pd
from pathlib import Path

# Dove sono i file. I percorsi partono dalla cartella principale del progetto.
FILE_PARTENZA = Path("data/raw/terna/xxxxx.xlsx")
FILE_PRODOTTO = Path("data/interim/terna.parquet")


def leggi():
    """Apre il file originale e lo restituisce come tabella."""
    df = ...   
    return df


def pulisci(df):
    """Pulisce la tabella e restituisce solo le colonne che ci interessano."""
    ...
    return df


def controlla(df):
    """Si ferma con un messaggio se qualcosa non va."""
    ...


def main():
    df = leggi()
    df = pulisci(df)
    controlla(df)
    FILE_PRODOTTO.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(FILE_PRODOTTO, index=False)
    print(f"Salvato {FILE_PRODOTTO}: {len(df)} righe")


if __name__ == "__main__":
    main()