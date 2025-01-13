import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos desde el archivo CSV
df = pd.read_csv('calificaciones_estudiantes.csv')

# 2. Calcular el promedio de calificaciones por asignatura
promedio_asignatura = df.groupby('Asignatura')['Calificacion'].mean()

# 3. Mostrar los resultados en la consola
print("Promedio de calificaciones por asignatura:")
print(promedio_asignatura)

# 4. Crear un gráfico de barras
plt.figure(figsize=(8, 6))  # Configurar el tamaño de la figura
promedio_asignatura.plot(kind='bar', color='skyblue', edgecolor='black')

# Configurar etiquetas y título del gráfico
plt.title('Promedio de Calificaciones por Asignatura', fontsize=16)
plt.xlabel('Asignatura', fontsize=14)
plt.ylabel('Calificación Promedio', fontsize=14)

# Guardar el gráfico como imagen PNG
plt.savefig('grafico_promedios.png')

# Mostrar el gráfico en pantalla
plt.show()