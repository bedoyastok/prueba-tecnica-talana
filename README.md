# prueba-tecnica-talana
Automatizacion de prueba con selenium y python

El repositorio con tiene un archivo cart.py, el cual contiene los casos de prueba planteados en el ejercicio y adicionalmente esta el archivo en PDF con el cuestionario.

Para la automatizacion de usaron:

Python 3.10.7

webdriver-manager 3.8.3

selenium 4.5.0

pyunitreport 0.1.4




   #Given el usuario quiere añadir mas de un producto al carro de compras
   #When selecciona los productos
   #Then se deben ver la cantidad exacta de productos en el carrito
   
   
   #Given el usuario quiere hacer checkout y editar su direccion
   #When termina de agregar los items
   #And da click en proceder con el checkout
   #And confirma la compra
   #And realiza el login
   #And edita la direccion
   #And continua con el metodo de pago
   #Then el flujo debe ser normal
   #And la edicion de la direccion no afecta el checkout
   
   #Given el usuario quiere ver el historial de ordenes
   #When finaliza el checkout
   #And ir a mis ordenes
   #Then deben aparecer todas las ordenes de acuerdo a su estado
