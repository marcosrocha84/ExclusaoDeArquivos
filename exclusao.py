import os
import time
from datetime import datetime, timedelta

pasta = 'K:\DIR_TMP\/'
total_arquivos = os.listdir(pasta)
print(str(total_arquivos.__len__()) + ' arquivo(s) na pasta ' + pasta)
data_atual = datetime.now() + timedelta(days=-180)    
print("Data de referencia para limpeza dos arquivos: " + str(data_atual.date()))
excluidos = 0
for aux in total_arquivos:
    caminho = pasta + aux
    aux2 = time.ctime(os.path.getmtime(caminho))
    aux3 = time.strptime(aux2)
    data_arquivo = time.strftime("%Y-%m-%d", aux3)
    if data_arquivo < str(data_atual):
        print('Ultima modificacao do arquivo "' + aux + '" foi em ' + data_arquivo + '. Arquivo deve ser excluido')
        excluidos = excluidos + 1
        #os.remove(caminho)
    
print("Foram excluidos " + str(excluidos) + " arquivo(s).")