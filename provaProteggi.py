import os
import subprocess

# Root directory containing files and subfolders
#root_directory = "D:/da upload"
password = ""


# Function to create a RAR archive containing only the file and replace the original file
def create_rar_and_replace(file_path, password):
    rar_file_name = file_path + '.rar'

    # Create a RAR archive containing only the file, replace the original file, and set a password
    command = f'winrar a -m0 -ep1 -p{password} "{rar_file_name}" "{file_path}"'
    subprocess.run(command, shell=True, stdout=subprocess.PIPE)

    # Check if the RAR file was successfully created
    if os.path.exists(rar_file_name):
        os.remove(file_path)
    else:
        print(f"Failed to create RAR for: {file_path}")




# Chiedi all'utente di inserire il percorso della cartella
root_directory = input("Inserisci il percorso della cartella: ")
root_directory = root_directory.replace("\\", "/")
print("Il percorso che hai inserito e': ",root_directory)

print("Tutti i files non .rar saranno protetti con password")

if os.path.exists(root_directory):
    # Loop through files and subfolders
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Create a RAR archive containing only the file, protect with a password, and replace the original file
            if not file.endswith(".rar"):
                if not file.endswith(".srt"):
                    if not file.endswith(".txt"):
                        create_rar_and_replace(file_path, password)

    print("Files have been successfully protected and replaced with RAR archives.")


else:
    print("La cartella specificata non esiste.")



