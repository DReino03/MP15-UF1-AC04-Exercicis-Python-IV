import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meteoCat2020:DataFrame
meteoCat2022:DataFrame
meteoCat_Metadades:DataFrame


def load_data():
    global meteoCat2020 
    global meteoCat2022
    global meteoCat_Metadades

    meteoCat2020 = pd.read_csv("MeteoCat_Estacions_2020.csv")
    meteoCat2022 = pd.read_csv("2022_MeteoCat_Detall_Estacions.csv")
    meteoCat_Metadades = pd.read_csv("MeteoCat_Metadades.csv")

# Temperatura media de febrero de 2020
def avg_temp_February():
    df = meteoCat2020[['DATA_LECTURA'] == "2022-02",] 


def avg_temp_February2():
    df = meteoCat2020[meteoCat2020['Mes'] == 2,]


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
            ejercicio_3()
        elif opcion == '3':
            ejercicio_4()
        elif opcion == '4':
            ejercicio_5()
        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Ingresa un número del 1 al 5.")

if __name__ == "__main__":
    main()