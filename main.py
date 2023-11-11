import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def load_datas(path):
    return pd.read_csv(path, header=0)


# Lee los ficheros csv
stationData = load_datas("MeteoCat_Estacions_2020.csv")
stationDataDetail = load_datas("2022_MeteoCat_Detall_Estacions.csv")
metaData = load_datas("MeteoCat_Metadades.csv")

# Indica que la columna DATA_LECTURA es una fecha para poder acceder a ello(acceder al mes, al dia...)
stationDataDetail['DATA_LECTURA'] = pd.to_datetime(stationDataDetail['DATA_LECTURA'])

# Filta los datos del fichero csv para que guardar los datos de frbereo de 2022 y que sean de ACRÒNIM (temperatura)
februaryData = stationDataDetail[
    (stationDataDetail['DATA_LECTURA'].dt.month == 2) &
    (stationDataDetail['DATA_LECTURA'].dt.year == 2022) &
    (stationDataDetail['ACRÒNIM'] == 'TM')]

# Ordena data frame colocando CODI_ESTACIO, DATA_LECTURA, VALOR en cloumnas diferentes
stationTemperatures = februaryData.groupby(['CODI_ESTACIO', februaryData['DATA_LECTURA'].dt.day])[
    'VALOR'].mean().unstack(level=0)


def media_febrero_unidas():
    plt.figure(figsize=(14, 8))

    for station in stationTemperatures.columns:
        plt.plot(stationTemperatures.index, stationTemperatures[station], label=f'{station}', marker='o')

    plt.xlabel('Days')
    plt.ylabel('Temperature')
    plt.title('Temperaturas medias de febrero segun estacion')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(stationTemperatures.index)
    plt.show()

def media_febrero_separadas():
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))
    fig.suptitle('Comparativa de Temperatura Media Diaria - Febrero 2022')

    # Establece los títulos para cada subgráfico
    axs[0, 0].set_title('Estación 1')
    axs[0, 1].set_title('Estación 2')
    axs[1, 0].set_title('Estación 3')
    axs[1, 1].set_title('Estación 4')

    # Grafica cada estación en su subgráfico correspondiente
    axs[0, 0].plot(stationTemperatures.index, stationTemperatures[stationTemperatures.columns[0]],
                   label='Estación 1', marker='o', color=plt.cm.tab10(0))
    axs[0, 1].plot(stationTemperatures.index, stationTemperatures[stationTemperatures.columns[1]],
                   label='Estación 2', marker='o', color=plt.cm.tab10(1))
    axs[1, 0].plot(stationTemperatures.index, stationTemperatures[stationTemperatures.columns[2]],
                   label='Estación 3', marker='o', color=plt.cm.tab10(2))
    axs[1, 1].plot(stationTemperatures.index, stationTemperatures[stationTemperatures.columns[3]],
                   label='Estación 4', marker='o', color=plt.cm.tab10(3))

    # Añade etiquetas y leyendas
    for ax in axs.flat:
        ax.set(xlabel='Days', ylabel='Temperature')
        ax.legend()
        ax.grid(True)
        ax.set_xticks(stationTemperatures.index)
        ax.set_ylim(stationTemperatures.min().min() - 1, stationTemperatures.max().max() + 1)

    # Ajusta el diseño y muestra la figura
    plt.tight_layout()
    plt.show()


def menu():
    while True:
        print("MENU:")
        print("1. Ver temperatura media de febrero en un solo gráfico")
        print("2. Ver temperatura media de febrero en diferentes gráficos")
        print("3. Predicción de temperatura del mes de febrero")
        print("4. Predicción de lluvias del mes de febrero")
        option = input("Por favor, seleccione una opción: ")

        if option == "1":
            media_febrero_unidas()

        elif option == "2":
            media_febrero_separadas()

        elif option == "3":
            print("Seleccionaste la opción 3")

        elif option == "4":
            print("Seleccionaste la opción 4")

        else:
            print("Opción no válida. Por favor, ingrese una opcion correcta")


menu()
