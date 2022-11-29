Gestor de tareas usable desde la terminal.

Acepta 3 valores:

-action: con valores "add" y "list", "add" permite añadir una tarea nueva y "list" muestra todas las tareas, pudiendo filtrar por orden de prioridad.

-name: es un campo obligatorio. Le podremos asignar un nombre o una descripción de la tarea a realizar.

-priority: con valores "low", "normal" o "high", por defecto será "normal". Permite asignarle un orden de prioridad a las tareas.

Por defecto se le añade el dia y la hora a la que se creó la tarea


Ejemplo de uso:

Entrada(en la carpeta donde tengamos tm.py)

python tm.py add "Hacer declaracion de la renta"

salida(en archivo tasks.csv):

2022-11-29 12:28:39; normal; "Hacer declaracion de la renta" 
