import pandas as pd
import os


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Nehme an, dass die letzte Zeile die Anzahl der Spalten und Zeilen enthalten
    num_rows = 2
    num_columns = 6

    # Entferne die letzten beiden Zeilen, die die Anzahl der Spalten und Zeilen enthalten
    data_lines = lines[:-1]

    # Splitte die Zeilen in Spalten
    data = [i.split('|') for i in [line.strip() for line in data_lines] if len(i) != 0]


    # Trimme die Daten auf die angegebene Anzahl von Spalten und Zeilen
    # data = data[:num_rows]
    for i in range(len(data)):
        data[i] = data[i][:num_columns]

    return data

def write_to_excel(data, excel_file_path):
    # Prüfe, ob die Excel-Datei existiert
    if os.path.exists(excel_file_path):
        # Lese die vorhandene Excel-Datei
        existing_df = pd.read_excel(excel_file_path, header=None)

        # Erstelle einen DataFrame aus den neuen Daten
        new_df = pd.DataFrame(data)

        # Hänge die neuen Daten an die vorhandenen Daten an
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Schreibe die kombinierten Daten zurück in die Excel-Datei
        updated_df.to_excel(excel_file_path, index=False, header=False)
        print(f"New data successfully appended to {excel_file_path}")
    else:
        # Erstelle DataFrame und transponiere, falls nur eine Zeile vorhanden ist
        df = pd.DataFrame(data)

        # Wenn nur eine Zeile vorhanden ist, transponiere den DataFrame
        if len(df) == 1:
            df = df.T

        df.to_excel(excel_file_path, index=False, header=False)
        print(f"Data successfully written to {excel_file_path}")
