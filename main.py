import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

def load_data(file_name):
    file = open(file_name, "r")
    reader = csv.reader(file)
    header = next(reader)
    data = [ row for row in reader ]
    array = np.array(list(data))
    file.close()
    return array

estacions = load_data("./MeteoCat_Estacions_2020.csv")
detall = load_data("./2022_MeteoCat_Detall_Estacions.csv")
metadata = load_data("./MeteoCat_Metadades.csv")   

# Temperatura media de febrero de 2020
def avg_temp_February():
    avg =  calculate_avg("TM")
    plt.plot(np.array(avg)[:,0], np.array(avg)[:,1])
    plt.xlabel('Days')
    plt.ylabel('Temperature')
    plt.title('Media diaria de febrero')
    plt.tight_layout()
    plt.show()
    '''
    print(np.array(avg))
    plt.plot(np.array(avg)[:,0], np.array(avg)[:,1])
    plt.ylabel("Temperatura ºC")
    plt.xlabel("Día")
    plt.xticks(range(1,29))
    plt.title("Temperatura media de febrero de 2020")
    plt.show()
    '''

#Calculate avg with acronim
def calculate_avg(average:str) -> list:
    days = {}
    for row in detall:
        date = row[0]
        acronim = row[3]
        day = date.split("-")[2]
        month = date.split("-")[1]

        if month == "02" and acronim == average.upper():
            num_day = int(day)
            value = float(row[4])
            if num_day not in days:
                days[num_day] = []
            days[num_day].append(value)
    avg = []
    for dia, values in days.items():
        avgs = sum(values) / len(values)
        avg.append((dia, avgs))
                
    return avg

"""
def predict_temp_February_2023():
    avg = calculate_avg("TM")
    temp_feb_2022 = np.array(avg)[:,1]
"""

def main():

    while True:
        print("Selecciona un ejercicio:")
        print("1. Cargar Datos")
        print("2. Visualizar Temperatura en Febrero")
        print("3. Predicción de Temperatura en Febrero 2023")
        print("4. Predicción de Lluvia en Febrero 2023")
        print("5. Salir")
        opcion = input("Ingresa el número del ejercicio: ")

        if opcion == '1':
            detall
            estacions
            metadata
            print("Datos cargados correctamente.")
            
        elif opcion == '2':
            calculate_avg("TM")

        elif opcion == '3':
            print("¡Adiós!")
            break
            
        elif opcion == '4':
            print("¡Adiós!")
            break

        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Ingresa un número del 1 al 5.")

if __name__ == "__main__":
    main()