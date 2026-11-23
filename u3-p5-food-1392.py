import pandas as pd
import matplotlib.pyplot as plt
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEIDOS DESDE CSV, Indian Food 1392 ---")
print(df_food_india)
print("\n--- Mostrar Nombre comida + ingredients 1392 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- Tiempo de cocinado mostrar 10 registros con head 1392 ---")
nombre_y_tiempo = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_tiempo)