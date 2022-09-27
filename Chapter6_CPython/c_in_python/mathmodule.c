#define PY_SSIZE_T_CLEAN
#include "Python.h"

static PyObject *method_add(PyObject *self, PyObject *args)
{
    PyObject *list_a = NULL;
    PyObject *list_b = NULL;

    if (!PyArg_ParseTuple(args, "OO", &list_a, &list_b))
    {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }

    Py_ssize_t len_a = PyList_Size(list_a);
    Py_ssize_t len_b = PyList_Size(list_b);

    if (len_a != len_b)
    {
        PyErr_SetString(PyExc_ValueError, "lists must have equal length.");
        return NULL;
    }

    PyObject *result = PyList_New(len_a);

    for (int i = 0; i < len_a; i++)
    {
        PyObject *item_a = PyList_GetItem(list_a, i);
        PyObject *item_b = PyList_GetItem(list_b, i);

        if (!PyLong_Check(item_a) && !PyLong_Check(item_b))
        {
            PyErr_SetString(PyExc_ValueError, "Items must be integers..");
            return NULL;
        }

        PyList_SetItem(result, i, PyNumber_Add(item_a, item_b));
    }

    return result;
}

static PyObject *method_clip(PyObject *self, PyObject *args)
{
    PyObject *const list = NULL;
    long min_value = 0;
    long max_value = 0;

    if (!PyArg_ParseTuple(args, "Oii", &list, &min_value, &max_value))
    {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");

        return NULL;
    }

    const Py_ssize_t len = PyList_Size(list);

    for (Py_ssize_t i = 0U; i < len; ++i)
    {
        const PyObject *const item = PyList_GetItem(list, i);

        if (!PyLong_Check(item))
        {
            PyErr_SetString(PyExc_ValueError, "Items must be integer..");
            return NULL;
        }

        const long temp = PyLong_AsLong(item);

        if (temp < min_value)
        {
            PyList_SetItem(list, i, PyLong_FromLong(min_value));
        }
        else if (temp > max_value)
        {
            PyList_SetItem(list, i, PyLong_FromLong(max_value));
        }
    }

    return Py_None;
}

static PyMethodDef math_cpythonMethods[] = {
    {"add", method_add, METH_VARARGS, "CPython Function"},
    {"clip", method_clip, METH_VARARGS, "CPython Function"},
    {NULL, NULL, 0, NULL} };

static struct PyModuleDef math_cpythonmodule = {
    PyModuleDef_HEAD_INIT, "math_cpython", "CPython Module", -1, math_cpythonMethods };

PyMODINIT_FUNC PyInit_math_cpython(void)
{
    return PyModule_Create(&math_cpythonmodule);
}
