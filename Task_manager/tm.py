import datetime
import argparse


def add_task(args):
    if args.priority == '*':
        args.priority = 'normal'
    
    if args.name == '':
        print('Tienes que añadir un nombre')
    else: 
        task = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}; {args.priority}; "{args.name}"'
        with open('tasks.csv', 'a') as f:
            f.write(f'{task} \n')

def tasks_list(args):
    check = 'low normal high'
    if args.priority == '*': #COMPRUEBA SI LA PRIORIDAD SE DA O ES POR DEFECTO Y SI LO ES, COPIA 
        args.priority = check

    with open('tasks.csv', 'r') as file:
        for line in file:
            if check != args.priority: #SI SON DIFERENTES, OBTENEMOS LA PRIORIDAD DE LA TAREA EN RESULT
                check = line.split(';')[1].strip()
            if args.priority in check:
                print(line.strip())
                check = 'low normal high'
        
            

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, choices=['add', 'list'], help='Elija acción: "add" para añadir tarea nueva o "list" para mostrar las tareas')
    parser.add_argument('name', type=str, nargs='?', default='', help='Especifique nombre o descripción de la tarea')
    parser.add_argument('-priority', type=str, choices=['low', 'normal', 'high'], default='*', help='Elija la prioridad de la tarea. Será "Normal" por defecto ')
    args = parser.parse_args()
    if args.action == 'add':
        add_task(args)
    if args.action == 'list':
        tasks_list(args)


if __name__ == '__main__':
    main()