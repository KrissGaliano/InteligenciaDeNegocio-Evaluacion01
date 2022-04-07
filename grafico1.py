import pandas as pd
import matplotlib.pyplot as plt
archivo=pd.read_csv('WEO_Data.csv',thousands=',',decimal='.')
archivo.rename(columns={'Country':'Pais'},inplace=True)
archivo.set_index('Pais',inplace=True)
lista=list(map(str,range(2000,2024)))
def grafico1():
    peru=archivo.loc['Peru',lista]
    peru.plot()
    plt.show()

def grafico2():
    peru=archivo.loc['Peru',lista]
    peru.plot(kind='line')
    plt.title('PERU-PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico3():
    paises=archivo.loc[['Peru','Chile'],lista]
    paises=paises.transpose()
    paises.plot(kind='line')
    plt.title('PERU vs CHILE')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico4():
    archivo.sort_values(by='2022',ascending=False,inplace=True)
    top5=archivo[lista].head(5)
    top5=top5.transpose()
    top5.plot(kind='line')
    plt.title('Top 5 Países - PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

grafico1()
grafico2()
grafico3()
grafico4()