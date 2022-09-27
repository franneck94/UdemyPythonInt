#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>

void Initialize(void)
{
    Py_Initialize();
}

void Finalize(void)
{
    Py_Finalize();
}

void PrepareImport(void)
{
    const char *const script =
        "import sys\n"
        "sys.path.insert(0, \".\")\n";
    PyRun_SimpleString(script);
}

void ErrorCheck(PyObject *obj)
{
    if (obj == NULL)
    {
        PyErr_Print();
        exit(1);
    }
}

void DoubleTest(PyObject *myModule)
{
    PyObject *myFunction = PyObject_GetAttrString(myModule, "getterDouble");
    ErrorCheck(myFunction);
    PyObject *myResult = PyObject_CallObject(myFunction, NULL);
    ErrorCheck(myResult);

    double result = PyFloat_AsDouble(myResult);
    printf("%lf\n", result);
}

void ListTest(PyObject *myModule)
{
    PyObject *myFunction = PyObject_GetAttrString(myModule, "getterList");
    ErrorCheck(myFunction);
    PyObject *myResult = PyObject_CallObject(myFunction, NULL);
    ErrorCheck(myResult);

    for (Py_ssize_t index = 0; index < 3; index++)
    {
        PyObject *item = PyList_GetItem(myResult, index);
        ErrorCheck(item);
        double result = PyFloat_AsDouble(item);
        printf("%lf\n", result);
    }
}

void TupleTest(PyObject *myModule)
{
    PyObject *myFunction = PyObject_GetAttrString(myModule, "getterTuple");
    ErrorCheck(myFunction);
    PyObject *myResult = PyObject_CallObject(myFunction, NULL);
    ErrorCheck(myResult);

    for (Py_ssize_t index = 0; index < 3; index++)
    {
        PyObject *item = PyTuple_GetItem(myResult, index);
        ErrorCheck(item);
        double result = PyFloat_AsDouble(item);
        printf("%lf\n", result);
    }
}

int main(void)
{
    Initialize();
    atexit(Finalize);
    PrepareImport();

    PyObject *myModule = PyImport_ImportModule("test");
    ErrorCheck(myModule);

    DoubleTest(myModule);
    ListTest(myModule);
    TupleTest(myModule);

    return 0;
}
