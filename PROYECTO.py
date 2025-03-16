import matplotlib.pyplot as plt
import time
from abc import ABC, abstractmethod

# Decorador para medir el tiempo de ejecución
def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ejecutado en {end_time - start_time:.6f} segundos")
        return result
    return wrapper

# Clase abstracta Movimiento
class Movimiento(ABC):
    @abstractmethod
    def calcular_posicion(self, t):
        pass
    
    @abstractmethod
    def calcular_velocidad(self, t):
        pass

# Clase MRUA
class MRUA(Movimiento):
    def __init__(self, posicion_inicial, velocidad_inicial, aceleracion):
        self._posicion_inicial = posicion_inicial
        self._velocidad_inicial = velocidad_inicial
        self._aceleracion = aceleracion
    
    @property
    def posicion_inicial(self):
        return self._posicion_inicial
    
    @property
    def velocidad_inicial(self):
        return self._velocidad_inicial
    
    @property
    def aceleracion(self):
        return self._aceleracion
    
    def calcular_posicion(self, t):
        return self._posicion_inicial + self._velocidad_inicial * t + 0.5 * self._aceleracion * t**2
    
    def calcular_velocidad(self, t):
        return self._velocidad_inicial + self._aceleracion * t

# Clase para Simulación
class SimulacionMRUA:
    def __init__(self, movimiento, tiempo_max, pasos):
        self.movimiento = movimiento
        self.tiempo_max = tiempo_max
        self.pasos = pasos
    
    @timing
    def ejecutar(self):
        tiempos = [i * self.tiempo_max / self.pasos for i in range(self.pasos + 1)]
        posiciones = [self.movimiento.calcular_posicion(t) for t in tiempos]
        velocidades = [self.movimiento.calcular_velocidad(t) for t in tiempos]
        
        self.graficar(tiempos, posiciones, velocidades)
    
    def graficar(self, tiempos, posiciones, velocidades):
        fig, axs = plt.subplots(2, 1, figsize=(8, 6))
        
        axs[0].plot(tiempos, posiciones, label='Posición (m)', color='blue')
        axs[0].set_xlabel('Tiempo (s)')
        axs[0].set_ylabel('Posición (m)')
        axs[0].legend()
        axs[0].grid()
        
        axs[1].plot(tiempos, velocidades, label='Velocidad (m/s)', color='red')
        axs[1].set_xlabel('Tiempo (s)')
        axs[1].set_ylabel('Velocidad (m/s)')
        axs[1].legend()
        axs[1].grid()
        
        plt.tight_layout()
        plt.show()

# Parámetros de simulación
movimiento = MRUA(posicion_inicial=0, velocidad_inicial=5, aceleracion=2)
simulacion = SimulacionMRUA(movimiento, tiempo_max=10, pasos=100)
simulacion.ejecutar()

