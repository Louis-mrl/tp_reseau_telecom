from os.path import isfile, getmtime
from datetime import datetime
from os import stat

file_name1 = input("Entrer le nom du fichier 1")
file_name2 = input("Entrer le nom du fichier 2")

file1 = isfile(file_name1)
file2 = isfile(file_name2)

if file1 and file2:
    file_size1 = stat(file_name1).st_size
    file_size2 = stat(file_name2).st_size
    print(f"Le fichier {file_name1} fait {file_size1} octets\nLe fichier {file_name2} fait {file_size2} octets")
    

    if getmtime(file1) > getmtime(file2):
        print(f"Le fichier {file_name1} est le plus récent !")
    else:
        print(f"Le fichier {file_name2} est le plus récent !")
    
    
    print(f"Car le fichier {file_name1} a été modifier le {datetime.fromtimestamp(getmtime(file1))} et que le fichier {file_name2} a été modifier le {datetime.fromtimestamp(getmtime(file2))}")

else:
    print("un des fichiers que vous avez s'éléctionné n'existe pas.")