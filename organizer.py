import os
import shutil

def create_directorys(files_dict:dict, files_array:list[str], current_path:str):
    already_exist_array:list[str] = []
    
    for x in files_array:
        for k, v in files_dict.items():
            directory = f'{current_path}/{k}'
            directory_exist = os.path.exists(directory)    
            
            if not directory_exist and get_path_of_file(x) in v:
                try:
                    os.mkdir(directory)
                    print(f'Directorio {directory} creado exitosamente')  
                except FileExistsError:
                    print("Ya existe")
                    continue
 
def get_path_of_file(file:str) -> str:
    return file.split(".")[-1]   

def get_files(path:str) -> list[str]:
    return os.listdir(path)


def isFile(file:str):
    if os.path.isfile(file) and not file == 'organizer.py':
        return True
    
def isDirectory(directory:str):
    print(os.path.isdir(directory))
    return os.path.isdir(directory)

def get_current_directories(current_path:str):
    return list(filter(lambda x: os.path.isdir(f'{current_path}/{x}'), get_files(current_path)))

def get_current_files(current_path:str):
    return list(filter(lambda x: True if os.path.isfile(f'{current_path}/{x}') and not x == "organizer.py" else False, get_files(current_path)))

if __name__ == "__main__":
    current_path = os.getcwd()
    organized_directory = "organized_files"
    final_directory = f'{current_path}/{organized_directory}'
        
    # Diccionario para organizar las carpetas conforme la extensión
    files_dictionary = {
        "Documentos": ['docx', 'doc'],
        "Textos": ['txt', 'md'],
        "PDFs": ['pdf'],
        "Hojas de cálculo": ['xlsx', 'xls'],
        "Presentaciones": ['pptx'],
        "Datos": ['csv', 'json', 'xml'],
        "Imágenes": ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        "Videos": ['mp4', 'mkv', 'avi', 'mov'],
        "Audios": ['mp3', 'wav', 'flac'],
        "Comprimidos": ['zip', 'rar', 'tar', 'gz', '7z', 'deb'],
        "Ejecutables": ['exe', 'ini', 'run', 'deb'],
        "Aplicaciones": ['apk'],
        "Web": ['html', 'css', 'js'],
        "Scripts": ['py', 'java', 'c', 'cpp', 'php', 'ts'],
        "Markdown": ['md'],
        "Gráficos": ['svg'],
        "Iconos": ['ico']
    }


    files_path_array = [get_path_of_file(i) for i in get_files(current_path) if not i == organized_directory]
    
    if organized_directory not in get_current_directories(current_path):
        os.mkdir(final_directory)
    
    
    create_directorys(files_dictionary, files_path_array, final_directory)    
        
    if get_current_files(current_path):
        for k, v in files_dictionary.items():
            destin = f'{final_directory}/{k}'
            for x in get_current_files(current_path):
                if get_path_of_file(x) in v:
                    try:
                        shutil.move(x, destin, copy_function=shutil.copy2)
                        print(f'{x} ha sido movido a {destin}')  
                    except FileExistsError:
                        print(f'{x} ya existe en el directorio')
    else:
        print("Todos los archivos ya han sido movidos a sus carpetas")
        
    
    
        
                