import pandas as pd
import matplotlib.pyplot as plt

archivo = pd.read_csv('WEO_Data.csv',thousands=',', decimal='.')
archivo.rename(columns={'Country':'Pais'},inplace=True)
archivo.set_index('Pais',inplace=True)
lista=list(map(str,range(2014,2019)))
lista1=list(map(str,range(2000,2024)))
lista2=list(map(str,range(2019,2020)))

def PreguntaA():
    GrafPeru = archivo.loc['Peru',lista]
    GrafPeru.plot(kind='line')
    plt.title('Peru-PBI')
    plt.ylabel('Billones de $')
    plt.xlabel("Años")
    plt.show()

PreguntaA()


def PreguntaB():
    GrafChinaEsta=archivo.loc[['China','United States'],lista1]
    GrafChinaEsta=GrafChinaEsta.transpose()
    GrafChinaEsta.plot(kind='line')
    plt.title("GRÁFICO LINEAL DE CHINA Y ESTADOS UNIDOS")
    plt.ylabel("Millones de $")
    plt.xlabel("AÑOS")
    plt.show()

PreguntaB()

def PreguntaC():
    archivo.sort_values(by='2019', ascending=True, inplace=True)
    Paises=archivo.loc[['United States','China','Japan','Germany','France','Brazil','Peru'],lista2]
    Paises=Paises.transpose()
    Paises.plot(kind='bar')
    plt.title('GRAFICO EN BARRAS DEL AÑO 2019')
    plt.ylabel('BILLONES DE $')
    plt.xlabel('AÑO')
    plt.show()

PreguntaC()


def PreguntaD():
    archivo.sort_values(by='2019', ascending=False, inplace=True)
    lista4 = list(map(str, range(2019, 2020)))
    paises = archivo[lista4].head(10)
    paises = paises.transpose()
    paises.plot(kind='bar')
    plt.title(' LOS 1O PAISES CON MAYOR PBI EN EL 2019')
    plt.xlabel('PAISES TOP')
    plt.ylabel('BILLONES DE $')
    plt.show()

PreguntaD()