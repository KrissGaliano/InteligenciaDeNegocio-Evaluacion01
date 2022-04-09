import pandas as pd
import matplotlib.pyplot as plt
archivo=pd.read_csv('WEO_Data.csv',thousands=',',decimal='.')
archivo.rename(columns={'Country':'Pais'},inplace=True)
archivo.set_index('Pais',inplace=True)
lista=list(map(str,range(2000,2024)))

def Pgrafico():
    grafico = pd.DataFrame([[600],[800],[1200],[2000]],
                            index=['Enero','Febrero','Marzo','Abril'],
                            columns=['Cantidad'])
    grafico.plot(kind='line')
    plt.title('INGRESOS DE CONSULTORA')
    plt.xlabel('Meses')
    plt.ylabel('Ingresos')
    print(grafico)
    plt.show()

Pgrafico()


def graficoccv():
    argentina = archivo.loc['Argentina', lista]
    argentina.plot()
    argentina.plot(kind='line')
    plt.title('ARGENTINA')
    plt.xlabel('AÑOS')
    plt.ylabel('INGRESOS')
    print(argentina)
    plt.show()


graficoccv()