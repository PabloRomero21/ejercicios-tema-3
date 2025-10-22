import datetime
def invierte_numero(n:int)-> int:
    negativo = n<0
    n = abs(n)
    res = 0
    while n != 0:
        res = res*10 + n%10
        n //= 10
    return res

def convierte_binario(n:int)-> str:
    res=""
    while n>0:
        res = str(n%2) + res
        n //= 2
    return res

def clasifica_rango():
    pass

def sumar_divisores_propios(n):
    suma = 0
    for i in range(1,n): #1,2,3,4,...,n-1
        if (n % i) == 0:
            suma += i
    return suma


def clasifica_numero(n):

    suma = sumar_divisores_propios(n)
    if n == suma:
        return "Perfecto"
    elif n < suma:
        return "Abundante"
    else:
        return "Deficiente"

def clasifica_rango(n):

    for i in range(1,n+1):
        print(f"{i}: {clasifica_numero}")

def busca_perfecto(n):
    numero = 1
    contador = 0
    while contador < n:
        numero += 1
        if clasifica_numero(numero) == "Perfecto":
            contador += 1
    return numero

from datetime import date, timedelta
 
def es_dia_festivo(fecha: date) -> bool:    
    """
    Función auxiliar que simula la verificación de días festivos.
    Parámetros:
        fecha: date: La fecha a verificar.
    Devuelve:
        bool: True si la fecha es un día festivo, False en caso contrario.
    """
    dias_festivos = {
        date(2026, 1, 1),   # Año Nuevo
        date(2026, 1, 6),   # Día de Reyes
        date(2026, 3, 19),  # San José
        date(2026, 5, 1),   # Día del Trabajo
        date(2026, 8, 15),  # Asunción de la Virgen
        date(2026, 10, 12), # Fiesta Nacional de España
        date(2026, 11, 1),  # Todos los Santos
        date(2026, 12, 6),  # Día de la Constitución
        date(2026, 12, 8),  # Inmaculada Concepción
        date(2026, 12, 25)  # Navidad
    }
    return fecha in dias_festivos

def es_dia_no_laborable(fecha):
    dia_semana = fecha.weekday()
    return dia_semana >= 5 or es_dia_festivo(fecha)

def calcular_siguiente_valida(fecha_anterior, intervalo_dias):
    fecha = fecha_anterior + timedelta(days=intervalo_dias)
    if es_dia_no_laborable(fecha):
        fecha= fecha + timedelta(days= 1)
    return fecha

def planificar_eventos(fecha_inicio,intervalo_dias,num_eventos):
    



        



