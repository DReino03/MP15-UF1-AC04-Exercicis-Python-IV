import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cargar_datos(file_path):
    try:
        # Intenta cargar el archivo CSV
        df = pd.read_csv('C:\Users\reino\OneDrive\Escritorio\ITB\Segon\S.experts\MeteoCat\2022_MeteoCat_Detall_Estacions.csv', sep=';') 
        return df
    except Exception as e:
        # Captura cualquier excepción y muestra un mensaje de error
        print(f"Error al cargar el archivo {file_path}: {str(e)}")
        return None

def ejercicio_2():
    # Ejercicio 2: Cargar Datos
    df1 = cargar_datos('2022_MeteoCat_Detall_Estacions.csv')
    df2 = cargar_datos('2020_MeteoCat_Estacions.csv')
    df3 = cargar_datos('MeteoCat_Metadades.csv')
    
    # Realizar operaciones con los DataFrames según sea necesario


def ejercicio_3():
    # Ejercicio 3: Visualizar Temperatura en Febrero
    df = cargar_datos('2022_MeteoCat_Detall_Estacions.csv')

    # Filtrar los datos para febrero de 2022
    febrero_data = df[df['DATA_LECTURA'].str.startswith('2022-02')]

    # Calcular la temperatura media diaria
    temperatura_media_diaria = febrero_data.groupby('DATA_LECTURA')['VALOR'].mean()

    # Crear un gráfico de temperatura
    plt.figure(figsize=(10, 6))
    plt.plot(temperatura_media_diaria.index, temperatura_media_diaria.values)
    plt.xlabel('Días de Febrero 2022')
    plt.ylabel('Temperatura Media')
    plt.title('Temperatura Media Diaria en Febrero 2022')
    plt.xticks(rotation=45)
    plt.show()

def ejercicio_4():
    # Ejercicio 4: Predicción de Temperatura en Febrero 2023
    # Aquí deberías implementar un modelo de predicción basado en datos históricos.
    pass

def ejercicio_5():
    # Ejercicio 5: Predicción de Lluvia en Febrero 2023
    probabilidad_lluvia = 0.20
    dias = 28  # Número de días en febrero
    lluvia = np.random.choice([True, False], size=dias, p=[probabilidad_lluvia, 1 - probabilidad_lluvia])

    # Crear un gráfico de barras para visualizar la proporción de días con lluvia y sin lluvia
    plt.figure(figsize=(6, 4))
    plt.bar(['Días con lluvia', 'Días sin lluvia'], [sum(lluvia), dias - sum(lluvia)])
    plt.xlabel('Lluvia')
    plt.ylabel('Cantidad de Días')
    plt.title('Predicción de Lluvia en Febrero 2023')
    plt.show()

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
            ejercicio_2()
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