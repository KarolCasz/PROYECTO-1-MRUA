# 1. Importación de módulos necesarios
import matplotlib.pyplot as plt  # Importa la librería para graficar
import matplotlib.animation as animation  # Permite crear animaciones
from abc import ABC, abstractmethod  # Permite definir clases abstractas que sirven como base para otras clases

# 2. Definición de la clase base ParametrosFisicos
class ParametrosFisicos: #almacena los datos fisicos(x,v,a)
    def __init__(self, posicion_inicial, velocidad_inicial, aceleracion):
        #__init__ constructor que inicializa la x,v,a
        #_se usa en los atributos para indicar que son privados
        if aceleracion == 0:
            raise ValueError("La aceleración no puede ser cero en MRUA.") #raise, indica que se ha producido un error,Evita errores físicos
        self._posicion_inicial = posicion_inicial  # Guarda la posición inicial   #se asignan los valores ingresados a atributos privados
        self._velocidad_inicial = velocidad_inicial  # Guarda la velocidad inicial
        self._aceleracion = aceleracion  # Guarda la aceleración

    # Métodos para obtener los valores (solo lectura y no se puedan modificar despues de crear el objeto)
    @property  #se puede acceder al valor de un atributo sin necesidad de llamarlo como una funcióny sin exponerlo directamente
    def posicion_inicial(self):
        return self._posicion_inicial   #return: devuelve el resultado de la posicion inicial #self:almacena los valores especificos

    @property
    def velocidad_inicial(self):
        return self._velocidad_inicial #sin self los atributos solo existirian dentro del metodo donde fueron creadas y no estarian asociadas al obj

    @property
    def aceleracion(self):
        return self._aceleracion

# 3. Definición de una clase abstracta para Movimiento
class Movimiento(ABC): #hereda de ABC (clase abstracta), no puede ser instanciada directamente
    @abstractmethod  #se usa para obligar a que las clases hijas implementen ciertos metodos
    def calcular_posicion(self, t):
        pass #se usa pq la funcion no debe hacer nada en la clase base, solo declara que debe existir en las subclases(no uso: error pq f esta vacia)

    @abstractmethod
    def calcular_velocidad(self, t):
        pass

# 4. Definición de la clase MRUA que implementa Movimiento y hereda ParametrosFisicos
class MRUA(ParametrosFisicos, Movimiento): #class MRUA hereda de parametrosFisicos(datos fisicos) y Movimiento(metodos abstractos) 
    def calcular_posicion(self, t): #calcula la posicion en funcion del tiempo
        if t < 0:
            raise ValueError("El tiempo no puede ser negativo.")  # Valida que el tiempo no sea negativo
        return self.posicion_inicial + self.velocidad_inicial * t + 0.5 * self.aceleracion * t**2  # Fórmula del MRUA

    def calcular_velocidad(self, t):
        return self.velocidad_inicial + self.aceleracion * t  # Calcula la velocidad en un instante t

    def calcular_aceleracion(self, t):
        return self.aceleracion  # La aceleración es constante en MRUA

# 5. Clase para gestionar la simulación de dos objetos en MRUA
class Simulacion:
    def __init__(self, movimiento1, movimiento2, tiempo_max=20, pasos=200):  #constructor de la simulacion
        if tiempo_max <= 0 or pasos <= 0:  #el tiempo y los pasos deben ser positivos
            raise ValueError("El tiempo máximo y los pasos deben ser positivos.")  # Valida los parámetros
        self.movimiento1 = movimiento1  # Guarda el primer objeto en movimiento
        self.movimiento2 = movimiento2  # Guarda el segundo objeto en movimiento
        self.tiempo_max = tiempo_max  # Tiempo total de la simulación
        self.pasos = pasos  # Número de pasos en la simulación

#5.1 Método ejecutar(), calcula la x,v,a en cada instante
    def ejecutar(self): 
        tiempos = [i * self.tiempo_max / self.pasos for i in range(self.pasos + 1)]  # Genera una lista de tiempos
        posiciones1 = [self.movimiento1.calcular_posicion(t) for t in tiempos]  # Calcula posiciones para el objeto 1
        posiciones2 = [self.movimiento2.calcular_posicion(t) for t in tiempos]  # Calcula posiciones para el objeto 2
        velocidades1 = [self.movimiento1.calcular_velocidad(t) for t in tiempos]  # Calcula velocidades del objeto 1
        velocidades2 = [self.movimiento2.calcular_velocidad(t) for t in tiempos]  # Calcula velocidades del objeto 2
        aceleraciones1 = [self.movimiento1.calcular_aceleracion(t) for t in tiempos]  # Aceleraciones objeto 1
        aceleraciones2 = [self.movimiento2.calcular_aceleracion(t) for t in tiempos]  # Aceleraciones objeto 2

        self.graficar(tiempos, posiciones1, posiciones2, velocidades1, velocidades2, aceleraciones1, aceleraciones2)
        self.animar(tiempos, posiciones1, posiciones2)

    def graficar(self, tiempos, posiciones1, posiciones2, velocidades1, velocidades2, aceleraciones1, aceleraciones2):
        fig, axs = plt.subplots(3, 1, figsize=(8, 12))  # Crea 3 gráficos en una sola figura
                    #cuando se crea multiples graficos con plt.su, axs[] perimte acceder a cada uno para personalizarlos
        axs[0].plot(tiempos, posiciones1, 'r-', label="Objeto 1")  # Gráfico de posición objeto 1
        axs[0].plot(tiempos, posiciones2, 'b-', label="Objeto 2")  # Gráfico de posición objeto 2
        axs[0].set_ylabel("Posición (m)") 
        axs[0].set_title("Posición vs Tiempo")
        axs[0].legend()
        axs[0].grid()  #se usa para agregar una cuadricula

        axs[1].plot(tiempos, velocidades1, 'r-', label="Objeto 1")  # Gráfico de velocidad objeto 1
        axs[1].plot(tiempos, velocidades2, 'b-', label="Objeto 2")  # Gráfico de velocidad objeto 2
        axs[1].set_ylabel("Velocidad (m/s)")
        axs[1].set_title("Velocidad vs Tiempo")
        axs[1].legend()
        axs[1].grid()

        axs[2].plot(tiempos, aceleraciones1, 'r-', label="Objeto 1")  # Gráfico de aceleración objeto 1
        axs[2].plot(tiempos, aceleraciones2, 'b-', label="Objeto 2")  # Gráfico de aceleración objeto 2
        axs[2].set_xlabel("Tiempo (s)")
        axs[2].set_ylabel("Aceleración (m/s²)")
        axs[2].set_title("Aceleración vs Tiempo")
        axs[2].legend()
        axs[2].grid()

        plt.tight_layout()  # ajusta el espaciado entre los elementos de la figura
        plt.show()

    def animar(self, tiempos, posiciones1, posiciones2): #se define el metodo para la animacion
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.tiempo_max)
        ax.set_ylim(min(posiciones1 + posiciones2), max(posiciones1 + posiciones2))
        ax.set_xlabel('Tiempo (s)')
        ax.set_ylabel('Posición (m)')
        ax.set_title("Animación del Movimiento")
        
        ax.plot(tiempos, posiciones1, 'r--', alpha=0.5) #r:color de la linea y --:linea punteada, alpha: linea semi transparente
        ax.plot(tiempos, posiciones2, 'b--', alpha=0.5)

        punto1, = ax.plot([], [], 'ro', label='Objeto 1') #[]:no se estan graficando puntos en ese momento, ro:puntos sean circulos rojo, label:etiqueta
        punto2, = ax.plot([], [], 'bo', label='Objeto 2')
        ax.legend()
# se define una función que actualiza la posicion de los objetos en cada fotograma
        def actualizar(frame):
            punto1.set_data([tiempos[frame]], [posiciones1[frame]])
            punto2.set_data([tiempos[frame]], [posiciones2[frame]])
            return punto1, punto2

        ani = animation.FuncAnimation(fig, actualizar, frames=len(tiempos), interval=50, blit=False) #blit=false: controla la actzcion de la fig
        plt.show()

# 6. Función principal main() para ejecutar la simulación
if __name__ == "__main__": #se verifica q el codigo se ejecute solo cuando el arch es ejecutado directamente
    print("\n--- Simulación de MRUA con dos objetos ---") #\n--- crea una nueva linea
    try: #si ocurre un error lo maneja de manera controlada (maneja excepciones)
        print("\nObjeto 1:") #convierte los datos en float para hacer calculos
        pos1 = float(input("Posición inicial (m): ")) #se solicita al usuario ingresar los datos del objeto 1
        vel1 = float(input("Velocidad inicial (m/s): "))
        acel1 = float(input("Aceleración (m/s²): "))

        print("\nObjeto 2:")
        pos2 = float(input("Posición inicial (m): "))
        vel2 = float(input("Velocidad inicial (m/s): "))
        acel2 = float(input("Aceleración (m/s²): "))

        simulacion = Simulacion(MRUA(pos1, vel1, acel1), MRUA(pos2, vel2, acel2)) #se crea una simulacion y se ejecuta
        simulacion.ejecutar()
    except ValueError as e: #captura error de tipo ValueError
        print(f"Error: {e}") #muestra el mensaje de error en pantalla
        #{e} contiene la descripcion del error que genero python        