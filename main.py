import os
from PIL import Image
from pip import main

def reduzir_imagem(input_dir, output_dir):
    lista_de_arquivos = os.listdir(input_dir)
    imagem = Image.open(os.path.join(input_dir, lista_de_arquivos[0]))
    redimensionada = imagem.resize((360,480))
    redimensionada.save(os.path.join(output_dir, lista_de_arquivos[0]))

if __name__ == "__main__":
    diretorio = '/home/arthur/Documentos/GitHub/h0landa/Hulk/input'

    reduzir_imagem(diretorio,'output')
    os.remove('input/img.jpg')