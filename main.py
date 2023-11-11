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

# Ordena el data frame colocando CODI_ESTACIO, DATA_LECTURA, VALOR en cloumnas diferentes
stationTemperatures = februaryData.groupby(['CODI_ESTACIO', februaryData['DATA_LECTURA'].dt.day])[
    'VALOR'].mean().unstack(level=0)

february_rain_data_2022 = stationDataDetail[
    (stationDataDetail['DATA_LECTURA'].dt.month == 2) &
    (stationDataDetail['DATA_LECTURA'].dt.year == 2022) &
    (stationDataDetail['ACRÒNIM'] == 'PPT')
    ]

february_rain_per_station = \
february_rain_data_2022.groupby(['CODI_ESTACIO', february_rain_data_2022['DATA_LECTURA'].dt.day])[
    'VALOR'].mean().unstack(level=0)

daily_rain = february_rain_per_station.median(axis=1)

rainy_days_bool = daily_rain > 0


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


def predict_febrero_temperature():
    daily_median_temperatures = stationTemperatures.median(axis=1).round().astype(int)

    plt.figure()
    values, bins, _ = plt.hist(daily_median_temperatures, bins=20, range=(-10, 25))
    plt.xlabel('Temperatura')
    plt.ylabel('Cantidad de días')
    plt.title('Distribución de temperaturas febrero 2022')
    plt.xticks(np.arange(-10, 26, 2))
    plt.ylim(0, max(values) + 2)
    plt.grid(True)
    plt.show()


def predict_2023_temperature():
    february_2023_prediction = stationTemperatures.mean().mean()

    days_in_february = 28
    february_2023_random_temperatures = np.round(
        np.random.normal(february_2023_prediction, 2, days_in_february)).astype(int)

    plt.bar(range(1, days_in_february + 1), february_2023_random_temperatures)
    plt.xlabel('Days')
    plt.ylabel('Temperature')
    plt.title('Predicción temperaturas febrero 2023')
    plt.xticks(np.arange(1, days_in_february + 1))
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def rain_predict():
    days_of_february = range(1, 29)

    plt.figure(figsize=(15, 6))
    plt.bar(days_of_february, rainy_days_bool)
    plt.xlabel('Days')
    plt.ylabel('Rain')
    plt.title('Predicción de lluvia Febrero 2023')
    plt.yticks([0, 1], ['No llueve', 'Llueve'])
    plt.xticks(days_of_february)
    plt.show()


def rain_proportion():
    rainy_days_count = np.sum(rainy_days_bool)
    non_rainy_days_count = len(rainy_days_bool) - rainy_days_count

    labels = ['Llueve', 'No llueve']
    sizes = [rainy_days_count, non_rainy_days_count]
    colors = ['#0973c1', '#f3b608']
    explode = (0.2, 0)
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
    plt.title('Proporción de lluvia febrero 2023')
    plt.show()


def menu():
    while True:
        print("MENU:")
        print("1. Ver temperatura media de febrero en un solo gráfico")
        print("2. Ver temperatura media de febrero en diferentes gráficos")
        print("3. Distribución de temperaturas febrero 2022")
        print("4. Predicción temperaturas febrero 2023")
        print("5. Predicción de lluvias del mes de febrero")
        print("6. Proporción de lluvia febrero 2023")
        option = input("Por favor, seleccione una opción: ")

        if option == "1":
            media_febrero_unidas()

        elif option == "2":
            media_febrero_separadas()

        elif option == "3":
            predict_febrero_temperature()

        elif option == "4":
            predict_2023_temperature()

        elif option == "5":
            rain_predict()

        elif option == "6":
            rain_proportion()

        else:
            print("Opción no válida. Por favor, ingrese una opcion correcta")


menu()
