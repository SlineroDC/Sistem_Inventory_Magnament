# 🛒 Sistema de Inventario

**Inventory Management System SL Advisors**\
Desarrollado por: **Sebastián Linero**

---

## 📋 Descripción

Este proyecto es un sistema de gestión de inventario desarrollado en **Python** que permite a los usuarios gestionar productos de forma sencilla desde la consola. Está diseñado para pequeñas empresas, estudiantes o proyectos educativos que deseen administrar un inventario básico.

---

## 🚀 Features

- **Agregar productos**\
  Permite registrar un producto nuevo especificando su nombre, precio y cantidad. Se valida que el producto no exista previamente y que los datos ingresados sean correctos.

- **Buscar productos**\
  Facilita la búsqueda de un producto por su nombre y muestra su información completa (nombre, precio, cantidad).

- **Actualizar precio**\
  Permite actualizar el precio de un producto ya existente en el inventario.

- **Eliminar productos**\
  Posibilidad de eliminar productos del inventario mediante su nombre.

- **Calcular valor total del inventario**\
  Calcula y muestra el valor total del inventario, multiplicando el precio por la cantidad de cada producto.

- **Interfaz por consola clara**\
  El menú es simple y permite al usuario seleccionar opciones mediante números.

- **Validaciones robustas**\
  El sistema verifica que los valores ingresados sean numéricos y positivos.

- **Código modular**\
  El sistema está diseñado en funciones, lo que facilita su mantenimiento y expansión.

---

## 🖥️ Requisitos

- **Python 3.x**
- Sistema operativo: Linux / macOS (usa `clear`)\
  *Si lo usas en Windows, debes cambiar **`os.system('clear')`** por **`os.system('cls')`** para limpiar la consola.*

---

## 📌 Instrucciones de uso

1. Clona el repositorio o descarga el archivo del proyecto.

2. Abre la terminal o consola en el directorio del proyecto.

3. Ejecuta el archivo principal:

   ```bash
   python examen_modulopy_Sl.py
   ```

4. Usa el menú para interactuar con el sistema:

   ```
   Inventory Management System SL advisors
   __________________________________________________
   1. Add Product
   2. Search Product
   3. Update Product Price
   4. Delete Product
   5. Calculate Total Inventory Value
   6. Exit
   ```

Selecciona la opción deseada ingresando el número correspondiente.

---

## 💡 Mejoras sugeridas

- Guardar y cargar inventario desde un archivo (JSON, CSV, etc).
- Permitir actualización de cantidad.
- Manejo de mayúsculas/minúsculas de forma insensible al buscar productos.
- Mejorar compatibilidad multiplataforma (limpieza de consola).

---

## ✉️ Autor

**Sebastián Linero**\
*Creador del sistema de inventario como proyecto educativo.*

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.

