
# Root directory containing files and subfolders
#root_directory = "D:\da upload\prova"
#password = ""



import os
import patoolib

def decomprimi_cartella(cartella, password):
    for root, dirs, files in os.walk(cartella):
        for file in files:
            if file.endswith(".rar"):
                file_rar = os.path.join(root, file)
                try:
                    patoolib.extract_archive(file_rar, outdir=root, password=password)
                    print(f"File decompresso: {file_rar}")

                    # Verifica se il file è stato decompresso correttamente
                    file_decompresso = os.path.splitext(file_rar)[0]
                    if os.path.exists(file_decompresso):
                        print(f"Verifica: Il file {file_rar} è stato decompresso correttamente.")

                        # Elimina il file RAR
                        os.remove(file_rar)
                        print(f"File RAR eliminato: {file_rar}")
                    else:
                        print(f"Errore: Il file {file_rar} potrebbe non essere stato decompresso correttamente.")
                except Exception as e:
                    print(f"Errore durante la decompressione di {file_rar}: {e}")


# Esempio di utilizzo
#cartella_da_decomprimere = 'D:\da upload\prova'
password_archivio = ''


# Chiedi all'utente di inserire il percorso della cartella
cartella_da_decomprimere = input("Inserisci il percorso della cartella: ")
cartella_da_decomprimere = cartella_da_decomprimere.replace("\\", "/")
print("Il percorso che hai inserito e': ",cartella_da_decomprimere)

print("Tutti i files .rar saranno decompressi")

if os.path.exists(cartella_da_decomprimere):
        decomprimi_cartella(cartella_da_decomprimere, password_archivio)
else:
    print("La cartella specificata non esiste.")