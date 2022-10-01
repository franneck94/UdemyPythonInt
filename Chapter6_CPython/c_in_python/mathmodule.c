#define PY_SSIZE_T_CLEAN
#include "Python.h"

static PyObject *method_clip_vector(PyObject *self, PyObject *args)
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
    {"clip_vector", method_clip_vector, METH_VARARGS, "CPython Function"},
    {NULL, NULL, 0, NULL} };

static struct PyModuleDef math_cpythonmodule = {
    PyModuleDef_HEAD_INIT, "math_cpython", "CPython Module", -1, math_cpythonMethods };

PyMODINIT_FUNC PyInit_math_cpython(void)
{
    return PyModule_Create(&math_cpythonmodule);
}
