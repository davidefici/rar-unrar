import os
import shutil
import patoolib
import tempfile

def dimensioni_simili(file1, file2, tolleranza=0.01):
    """Controlla se le dimensioni di due file sono simili entro una certa tolleranza (default 1%)."""
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    differenza = abs(size1 - size2)
    media_size = (size1 + size2) / 2

    if differenza / media_size <= tolleranza:
        return True
    return False

def decomprimi_e_copia(cartella_origine, cartella_destinazione, password=None, tolleranza=0.01):
    for root, dirs, files in os.walk(cartella_origine):
        for file in files:
            if file.endswith(".rar"):
                file_rar = os.path.join(root, file)

                # Nome file senza estensione .rar
                nome_file_decompresso = os.path.splitext(file)[0]

                try:
                    # Crea una cartella temporanea per decomprimere il file
                    with tempfile.TemporaryDirectory() as tempdir:
                        # Decomprime il file RAR nella cartella temporanea
                        patoolib.extract_archive(file_rar, outdir=tempdir, verbosity=-1, password=password)
                        print(f"File decompresso: {file_rar} in {tempdir}")

                        # Copia i file decompressi nella destinazione
                        for root_temp, dirs_temp, files_temp in os.walk(tempdir):
                            for file_temp in files_temp:
                                percorso_file_temp = os.path.join(root_temp, file_temp)

                                # Calcola il percorso relativo dalla cartella temporanea
                                percorso_relativo = os.path.relpath(percorso_file_temp, tempdir)

                                # Costruisci il percorso finale mantenendo la struttura delle directory relative
                                percorso_destinazione_finale = os.path.join(cartella_destinazione, os.path.relpath(root, cartella_origine), percorso_relativo)

                                # Crea le cartelle nella destinazione se non esistono
                                os.makedirs(os.path.dirname(percorso_destinazione_finale), exist_ok=True)

                                # Copia il file decompresso nella destinazione
                                shutil.copy2(percorso_file_temp, percorso_destinazione_finale)

                                # Verifica la dimensione del file copiato
                                if dimensioni_simili(percorso_file_temp, percorso_destinazione_finale, tolleranza):
                                    print(f"File copiato correttamente: {percorso_relativo}")
                                else:
                                    print(f"Errore: Le dimensioni di {percorso_relativo} non corrispondono. Ritentando...")
                                    # Ritenta la copia
                                    shutil.copy2(percorso_file_temp, percorso_destinazione_finale)

                except Exception as e:
                    print(f"Errore durante la decompressione o copia di {file_rar}: {e}")

# Esempio di utilizzo
cartella_origine = input("Inserisci il percorso della cartella di origine: ").replace("\\", "/")
cartella_destinazione = input("Inserisci il percorso della cartella di destinazione: ").replace("\\", "/")
password_archivio = input("Inserisci la password per gli archivi (lascia vuoto se non necessaria): ") or None

print("Tutti i file .rar saranno decompressi e copiati nella destinazione.")

if os.path.exists(cartella_origine):
    decomprimi_e_copia(cartella_origine, cartella_destinazione, password_archivio)
else:
    print("La cartella di origine specificata non esiste.")
