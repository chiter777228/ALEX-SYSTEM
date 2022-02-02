//Запуск файла simple.py
/**
 * gcc simple.c $(python3-config --includes --ldflags) -o simple && ./simple
 */
#include "types.h" 
#include "printf.h" 
#include <Python.h>
#include <stdio.h>
 
#define N 80

void 
python() {
    // Загрузка интерпритатора Python
    Py_Initialize();
    
    // Выполнение команды в интерпритаторе
    PyRun_SimpleString("import sys");
    // Путь до наших исходников python
PyRun_SimpleString("sys.path.append('. /files')");
    PyRun_SimpleString("import ALEX");
   //импорт файла ALEX.py
   FILE *file;
    char arr[N];
    int i;
 
    file = fopen("files/ALEX.py", "r");
 
    while ((arr[i] = fgetc(file)) != EOF) {
        if (arr[i] == '\n') {
            arr[i] = '\0';
            PyRun_SimpleString(arr[i]);
            //printf("%s\n",arr);
            i = 0;
        }
        else i++;
    }
    arr[i] = '\0';
   // printf("%s\n",arr);
 
    fclose(file);
//PyRun_SimpleString("print(simple.get_value(2))");
    //PyRun_SimpleString("print(simple.get_value(2.0))");
    //PyRun_SimpleString("print(simple.get_value(\"Hello!\"))");
    
    // Выгрузка интерпритатора Python
    Py_Finalize();  
}

void
fmain() {
    puts("Test ALEX:");
    
    python();
}

