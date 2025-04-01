![image](https://github.com/user-attachments/assets/0362a528-44a7-42d8-8b06-1ba396e6585b)# Simulación de Movimiento Rectilíneo Uniformemente Acelerado (MRUA)

## Descripción
Este proyecto implementa una simulación del **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)** para dos objetos en movimiento. Utiliza **Python y Matplotlib** para calcular y graficar la posición, velocidad y aceleración en función del tiempo, además de generar una animación del movimiento.

## Modelado Matemático
La simulación se basa en las ecuaciones del **MRUA**, que describen el movimiento de un objeto sometido a una aceleración constante:

1. **Posición en función del tiempo:**
   
   $$x(t) = x_0 + v_0 t + \frac{1}{2} a t^2$$

2. **Velocidad en función del tiempo:**
   
   $$v(t) = v_0 + a t$$

3. **Aceleración:**
   
   $$a(t) = a \quad \text{(constante)}$$

Donde:
- \( x_0 \) es la posición inicial,
- \( v_0 \) es la velocidad inicial,
- \( a \) es la aceleración,
- \( t \) es el tiempo transcurrido.

## Funcionalidades
- Simulación de dos objetos con diferentes parámetros iniciales.
- Cálculo y graficación de la posición, velocidad y aceleración.
- Validación de datos para evitar errores físicos.
- Animación interactiva del movimiento.
- Visualización de ecuaciones en formato matemático con **Matplotlib**.

## Requisitos
Asegúrate de tener **Python 3.x** instalado junto con las siguientes bibliotecas:
```bash
pip install matplotlib
```

## Uso
1. Ejecuta el código en Python:
   ```bash
   python main.py
   ```
2. Ingresa los parámetros iniciales cuando se te solicite:
   - Posición inicial (m)
   - Velocidad inicial (m/s)
   - Aceleración (m/s²)
3. Visualiza los gráficos de posición, velocidad y aceleración.
4. Disfruta de la animación del movimiento de los dos objetos.
5. Para visualizar las ecuaciones en formato matemático, ejecuta el siguiente código adicional:
   ```python
   import matplotlib.pyplot as plt
   
   def mostrar_ecuaciones():
       fig, ax = plt.subplots(figsize=(6, 4))
       ax.axis("off")  # Oculta los ejes
       
       # Ecuaciones del MRUA
       ecuaciones = (
           r"$x(t) = x_0 + v_0 t + \frac{1}{2} a t^2$",
           r"$v(t) = v_0 + a t$",
           r"$a(t) = a$ (constante)"
       )
       
       # Posiciones en la figura
       for i, eq in enumerate(ecuaciones):
           ax.text(0.1, 0.8 - i * 0.3, eq, fontsize=16, ha='left', va='center')
       
       plt.show()
   
   # Llamar a la función para mostrar las ecuaciones
   mostrar_ecuaciones()
   ```

## Ejemplo de Gráficos
![Ejemplo de Gráficos de MRUA](https://www.fisicalab.com/sites/all/files/contenidos/intromov/grafica_x-t_mrua.png)

## Objetivos del Proyecto
- Ayudar a visualizar el concepto de **MRUA** con gráficos y animaciones.
- Servir como herramienta educativa para **estudiantes de física**.
- Proporcionar un código modular y reutilizable en simulaciones de movimiento.

## Licencia
Este proyecto está bajo la **Licencia MIT** – Eres libre de usarlo y modificarlo con atribución adecuada.

---
**Autor:** _[Karol Ivonne Castro Hernández]_  
**Repositorio en GitHub:** [Enlace al repositorio](https://github.com/tu_usuario/tu_repositorio)
