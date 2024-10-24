
import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'venta_cls.csv'

try:
    # Leer el archivo CSV
    data_ordenada = pd.read_csv(archivo_csv)



    # Asegúrate de que todas las columnas relevantes sean tratadas como cadenas
    columnas_vtas = ['Ene_Vta', 'Feb_Vta', 'Mar_Vta', 'Abr_Vta', 'May_Vta', 'Jun_Vta', 'Jul_Vta', 'Ago_Vta', 'Sep_Vta', 'Oct_Vta', 'Nov_Vta', 'Dic_Vta']
    for col in columnas_vtas:
        data_ordenada[col] = pd.to_numeric(data_ordenada[col].astype(str).str[1:], errors='coerce')

 

    # Limpiar datos vacíos
    data_ordenada.fillna(0, inplace=True)

    # Crear nuevos campos
    data_ordenada['Unidad_total'] = (
        data_ordenada['Ene_Uds'] + data_ordenada['Feb_Uds'] + data_ordenada['Mar_Uds'] +
        data_ordenada['Abr_Uds'] + data_ordenada['May_Uds'] + data_ordenada['Jun_Uds'] +
        data_ordenada['Jul_Uds'] + data_ordenada['Ago_Uds'] + data_ordenada['Sep_Uds'] +
        data_ordenada['Oct_Uds'] + data_ordenada['Nov_Uds'] + data_ordenada['Dic_Uds']
    )

    data_ordenada['Costo_Total'] = (
        data_ordenada['Ene_Vta'] + data_ordenada['Feb_Vta'] + data_ordenada['Mar_Vta'] +
        data_ordenada['Abr_Vta'] + data_ordenada['May_Vta'] + data_ordenada['Jun_Vta'] +
        data_ordenada['Jul_Vta'] + data_ordenada['Ago_Vta'] + data_ordenada['Sep_Vta'] +
        data_ordenada['Oct_Vta'] + data_ordenada['Nov_Vta'] + data_ordenada['Dic_Vta']
    )

    # Contar cuántos meses tienen unidades mayores a 0
    columnas_uds = ['Ene_Uds', 'Feb_Uds', 'Mar_Uds', 'Abr_Uds', 'May_Uds', 'Jun_Uds', 
                    'Jul_Uds', 'Ago_Uds', 'Sep_Uds', 'Oct_Uds', 'Nov_Uds', 'Dic_Uds']
    data_ordenada['Conteo_ventas_mes'] = data_ordenada[columnas_uds].gt(0).sum(axis=1)

    # Clasificar según el conteo de ventas
    def clasificar_ventas(conteo):
        if conteo >=7:
            return 'A'
        elif conteo >=4:
            return 'B'
        else:
            return 'C'

    data_ordenada['Clasificacion'] = data_ordenada['Conteo_ventas'].apply(clasificar_ventas)
    # Ordenar los datos por ventaTotal
    data_ordenada=data_ordenada.sort_values(by='Costo_Total',ascending=False)
   # Ordenar los datos por nombre
    #data_ordenada = data.sort_values(by='Marca')

    # Exportar a un nuevo archivo CSV
    archivo_csv_ordenado = 'venta_ordenados.csv'
    data_ordenada.to_csv(archivo_csv_ordenado, index=False)

    print(f"Datos exportados exitosamente a {archivo_csv_ordenado}")

except Exception as e:
    print(f"Error al transformar los datos: {e}")
