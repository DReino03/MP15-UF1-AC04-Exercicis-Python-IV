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

estacions = load_data("MeteoCat_Estacions_2020.csv")
detall = load_data("2022_MeteoCat_Detall_Estacions.csv")
metadata = load_data("MeteoCat_Metadades.csv")


#Calculate avg with acronim
def calculate_avg(valor:str) -> list:
    day = {}
    for row in detall:
        date = row[0]
        acronim = row[3]
        day = date.split("-")[2]
        month = date.split("-")[1]

        if month == "02" and acronim == valor.upper():
            num_day = int(day)
            value = float(row[4])
            if num_day not in day:
                day[num_day] = []
            day[num_day].append(value)
    avg = []
    for dia, value in day.items():
        avg = sum(value) / len(value)
        avg.append((dia, avg))
                
    return avg


# Temperatura media de febrero de 2020
def avg_temp_February():
    avg =  calculate_avg("TM")
    print(np.array(avg))
    plt.plot(np.array(avg)[:,0], np.array(avg)[:,1])
    plt.ylabel("Temperatura ºC")
    plt.xlabel("Día")
    plt.xticks(range(1,29))
    plt.title("Temperatura media de febrero de 2020")
    plt.show()

def predict_temp_February_2023():
    
    avg = calculate_avg("TM")
    temp_feb_2022 = np.array(avg)[:,1]
    

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
            load_data()
        elif opcion == '2':
            print(avg_temp_February())
        elif opcion == '3':

        elif opcion == '4':
        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Ingresa un número del 1 al 5.")

if __name__ == "__main__":
    main()