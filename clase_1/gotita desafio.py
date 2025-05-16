#Tarifa base:
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.
# Bonificaciones y Recargos según tipo de cliente:

# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000,
# se aplica un descuento adicional del 5%.
# En todos los casos, se aplica el IVA del 21% sobre el total.

# Requerimientos del programa:
#1) Solicitar al usuario:
# Cantidad de metros consumidos
# Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
#2) Calcular:
# Subtotal de consumo.
# Bonificaciones, si corresponde
# Recargos, si corresponde
# Subtotal, con recargos y bonificaciones.
# IVA aplicado (21%), si corresponde.
#3) Total final a pagar.
# Mostrar en pantalla el desglose de los cálculos.
 
tarifa_base =  7000
tipo_cliente = input("que tipo de cliente sos(Residencial, Comercial o Industrial.): ")
tipo_consumo = int(input("ingrese su tipo de consumo: "))
costo_consumo = tipo_consumo * 200
bonificacion_30 = costo_consumo * 0.30
bonificacion_20 = costo_consumo * 0.20
bonificacion_10 = costo_consumo * 0.10
bonificacion_8 = costo_consumo * 0.08
bonificacion_12 = costo_consumo * 0.12
recarga_15 = costo_consumo * 0.15
recarga_10 = costo_consumo * 0.10
recarga_5 = costo_consumo * 0.05
subtotal_original = tarifa_base + costo_consumo
match tipo_cliente:
    case "Residencial":
        if tipo_consumo < 30: 
            consumo_modificado = costo_consumo - bonificacion_10
            subtotal = consumo_modificado + tarifa_base
            if subtotal_original < 35000:
                descuento_5 = subtotal * 0.05
                subtotal -= descuento_5
            iva = subtotal * 0.21 
            total_final =  subtotal + iva 
        elif tipo_consumo > 80:
            consumo_modificado = costo_consumo + recarga_15 
            subtotal = consumo_modificado + tarifa_base
            iva = subtotal * 0.21
            total_final =  subtotal + iva
        else:
            subtotal = tarifa_base + costo_consumo 
            iva = subtotal * 0.21 
            total_final =  subtotal + iva
    case "Comercial":
        if tipo_consumo > 300:
            consumo_modificado = costo_consumo - bonificacion_12
            subtotal = tarifa_base + consumo_modificado
            iva = subtotal * 0.21
            total_final = subtotal + iva
        elif tipo_consumo > 150:
            consumo_modificado = costo_consumo - bonificacion_8
            subtotal = tarifa_base + consumo_modificado
            iva = subtotal * 0.21
            total_final = subtotal + iva
        elif tipo_consumo < 50:
            consumo_modificado = costo_consumo + recarga_5
            subtotal = tarifa_base + consumo_modificado
            iva = subtotal * 0.21
            total_final = subtotal + iva
        else: 
            subtotal = tarifa_base + costo_consumo
            iva = subtotal * 0.21
            total_final = subtotal + iva
    case "Industrial":
        if tipo_consumo > 1000:
            consumo_modificado = costo_consumo - bonificacion_30
            subtotal = tarifa_base + consumo_modificado
            iva = subtotal * 0.21
            total_final = subtotal + iva
        elif tipo_consumo > 500:
            consumo_modificado = costo_consumo - bonificacion_20
            subtotal = tarifa_base + consumo_modificado
            iva = subtotal * 0.21 
            total_final = subtotal + iva
        elif tipo_consumo < 200:
            consumo_modificado = costo_consumo + recarga_10
            subtotal = tarifa_base + consumo_modificado
            iva = subtotal * 0.21 
            total_final = subtotal + iva
        else: 
            subtotal = tarifa_base + costo_consumo
            iva = subtotal * 0.21
            total_final = subtotal + iva







print("Subtotal:", subtotal)
print("IVA (21%):", iva)
print("Total final a pagar:", total_final)