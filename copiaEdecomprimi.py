import os
import shutil
import patoolib
import tempfile

def decomprimi_e_copia(cartella_origine, cartella_destinazione, password=None):
    for root, dirs, files in os.walk(cartella_origine):
        for file in files:
            if file.endswith(".rar"):
                file_rar = os.path.join(root, file)
                
                # Nome file senza estensione .rar
                nome_file_decompresso = os.path.splitext(file)[0]
                
                # Percorso del file nella destinazione
                percorso_destinazione = os.path.join(cartella_destinazione, nome_file_decompresso)
                
                # Verifica se il file già esiste nella destinazione
                if os.path.exists(percorso_destinazione):
                    print(f"Il file {nome_file_decompresso} esiste già nella destinazione, salto...")
                    continue
                
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
                                percorso_destinazione_finale = os.path.join(cartella_destinazione, file_temp)
                                
                                # Crea le cartelle se non esistono
                                os.makedirs(os.path.dirname(percorso_destinazione_finale), exist_ok=True)
                                
                                # Copia il file decompresso nella destinazione
                                shutil.copy2(percorso_file_temp, percorso_destinazione_finale)
                                print(f"File copiato: {file_temp}")
                                
                except Exception as e:
                    print(f"Errore durante la decompressione di {file_rar}: {e}")

# Esempio di utilizzo
cartella_origine = input("Inserisci il percorso della cartella di origine: ").replace("\\", "/")
cartella_destinazione = input("Inserisci il percorso della cartella di destinazione: ").replace("\\", "/")
password_archivio = input("Inserisci la password per gli archivi (lascia vuoto se non necessaria): ") or None

print("Tutti i file .rar saranno decompressi e copiati nella destinazione.")

if os.path.exists(cartella_origine):
    decomprimi_e_copia(cartella_origine, cartella_destinazione, password_archivio)
else:
    print("La cartella di origine specificata non esiste.")
