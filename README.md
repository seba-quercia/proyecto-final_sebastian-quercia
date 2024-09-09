# Meraki App

## Descripción

**Meraki App** es una aplicación web desarrollada en Django para la gestión de inventarios y precios de productos. La aplicación permite a los usuarios agregar, modificar, buscar y visualizar productos, así como gestionar el stock y los precios asociados a cada producto. Tambien se pueden crear perfiles de usuario los cuales por default van a tener permisos de solo lectura.

## Instalación

1. **Clona este repositorio:**

   ```bash
   git clone https://github.com/seba-quercia/proyecto-final_sebastian-quercia.git
   cd meraki_app


2. **Instala las dependencias:**

pip install -r requirements.txt



3. **Realiza las migraciones**

python manage.py makemigrations
python manage.py migrate



4. **Crea un superusuario (opcional, para acceder al admin de Django):**

python manage.py createsuperuser


5. **Ejecuta el servidor:**

python manage.py runserver


**Especificaciones**

1. Inicio y Cuadro de Búsqueda
Ruta: / (Página principal)
Descripción: En la página principal, verás un cuadro de búsqueda que permite buscar productos por nombre. Introduce el nombre de un producto y haz clic en "Buscar" para ver los resultados. (Para esto no hace falta tener user o estar logueado). Por ejemplo probar con **search/?q=Sahumerio**

Desde el NavBar se puede acceder a **/about/** y a los formularios de login y resgistro de usuarios

Por default ya se encuentran generados los siguientes usuarios

User: admin
Password: Cisco123
Permisos: superuser

User: romina
Password: Sahumerio
Permisos: Manager_L3 (View / Add / Change / Delete)

User: lautaro
Password: patineta123
Permisos: Empleado_L1 (View)


2. Gestion de Inventario y Agregar/Modificar/Eliminar productos

Una vez logueado, en el NavBar aparecera el menu de Gestion de Inventario, desde allí se podra agregar nuevos productos, o seleccionar uno de los ya existentes para ver sus detalles, y modificarlos o eliminarlos si se cuenta con los permisos requeridos

- Vista general del inventario: **/inventario/**
- Agregar producto **/producto/nuevo/**
- Vista detallada de producto **/producto/[id]/**



3. Ajustes de usuario y mensajeria
Una vez logueado se puede acceder al menu de ajustes de usuario desde el NavBar haciendo click en el avatar

Route **/accounts/account-settings/**

   Desde aqui, se puede cambiar el avatar, escribir una Bio, cambiar el username, password, nombre y apellido

Route **/accounts/messages/**

   Desde aquí se puede gestionar la mensajeria entre cuentas de usuario