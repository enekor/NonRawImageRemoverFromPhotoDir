import os;

baseDir = 'D:\\Camara'
rawDir = os.path.join(baseDir, 'raw')

imageNames = list(map(lambda x: x.split('.')[0], os.listdir(baseDir)))
rawImageNames = list(map(lambda x: x.split('.')[0], os.listdir(rawDir)))

for rawImageName in rawImageNames:
    if not rawImageName in imageNames:
        try:
            os.remove(os.path.join(rawDir, rawImageName+".CR2"))
            print(f'Borrado {rawImageName}.CR2, no te rayes buscandolo')
        except Exception as e:
            print(f"Error deleting {rawImageName}.CR2: {e}")