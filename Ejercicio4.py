empleados = [
{"id": 1, "nombre": "Carlos", "departamento": "Ventas", "salario": 1500},
{"id": 2, "nombre": "Ana", "departamento": "IT", "salario": 2200},
{"id": 3, "nombre": "Luis", "departamento": "Ventas", "salario": 1400}
]

def calcular_gasto_departamento(empleados, depto):
    suma_total = 0
    for i in empleados:
        if i['departamente'] == depto:
            suma_total += i['salario']
    return suma_total
print(calcular_gasto_departamento(empleados, "Ventas"))