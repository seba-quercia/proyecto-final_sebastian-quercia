# Meraki App

## Descripción

**Meraki App** es una aplicación web desarrollada en Django para la gestión de inventarios y precios de productos. La aplicación permite a los usuarios agregar, modificar, buscar y visualizar productos, así como gestionar el stock y los precios asociados a cada producto.

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


**Orden de Pruebas**

1. Inicio y Cuadro de Búsqueda
Ruta: / (Página principal)
Descripción: En la página principal, verás un cuadro de búsqueda que permite buscar productos por nombre. Introduce el nombre de un producto y haz clic en "Buscar" para ver los resultados.
Funcionalidad: Prueba que el cuadro de búsqueda funcione correctamente y que te redirija a la página de resultados con los productos correspondientes.

2. Agregar Productos
Ruta: /productos/
Descripción: Accede a la sección de productos donde podrás agregar nuevos productos. Completa el formulario con el nombre y la descripción del producto y haz clic en "Agregar".
Funcionalidad: Verifica que el producto se agregue correctamente y aparezca en la lista de productos.

3. Modificar Productos
Ruta: /productos/
Descripción: En la lista de productos, selecciona el producto que deseas modificar haciendo clic en "Editar". Cambia los valores deseados y guarda los cambios.
Funcionalidad: Confirma que los cambios se reflejen en la lista de productos.

4. Gestión de Stock
Ruta: /stocks/
Descripción: Accede a la sección de gestión de stock. Aquí puedes agregar o modificar la cantidad de stock disponible para cada producto.
Funcionalidad: Asegúrate de que la cantidad de stock se actualice correctamente y que se muestre en la vista de búsqueda.

5. Gestión de Precios
Ruta: /precios/
Descripción: Accede a la sección de gestión de precios. Aquí puedes establecer o modificar el precio de cada producto.
Funcionalidad: Verifica que los precios se actualicen correctamente y que se reflejen en la vista de búsqueda.

6. Resultados de Búsqueda
Ruta: /search/?q=<nombre_del_producto>
Descripción: Realiza búsquedas para diferentes productos y confirma que los resultados se muestren correctamente en la tabla, incluyendo el nombre, la descripción, el stock y el precio.
Funcionalidad: Asegúrate de que la búsqueda sea precisa y que los resultados coincidan con los datos ingresados.
Estructura del Proyecto
meraki_app/
models.py: Define las clases Producto, Stock, y Precio.
views.py: Contiene la lógica para las vistas de productos, stock, precios y búsqueda.
forms.py: Define los formularios para agregar y modificar productos, stock y precios.
templates/meraki_app/: Contiene las plantillas HTML del proyecto (base.html, productos.html, search.html, etc.)
static/meraki_app/: Archivos estáticos como CSS, JS e imágenes.