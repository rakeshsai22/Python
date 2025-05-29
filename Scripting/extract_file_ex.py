import os

def list_extensions(directory):
    extensions = set()
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,filename)): #checking if filename is a file or a folder
            _,ext = os.path.splitext(filename)
            if ext:
                extensions.add(ext)
    return extensions

print(list_extensions("/Users/srisairakeshnakkilla/Python/Scripting"))