#include <Python.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p) {
	PyBytesObject *bytes;
	Py_ssize_t i, size;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_GET_SIZE(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	printf("  first %ld bytes:", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++) {
		printf(" %02x", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p) {
	PyListObject *list;
	Py_ssize_t i, size;

	printf("[*] Python list info\n");

	if (!PyList_Check(p)) {
		printf("[!] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++) {
		printf("Element %ld: ", i);
		if (PyBytes_Check(PyList_GET_ITEM(p, i))) {
			print_python_bytes(PyList_GET_ITEM(p, i));
		} else if (PyTuple_Check(PyList_GET_ITEM(p, i))) {
			printf("tuple\n");
		} else if (PyList_Check(PyList_GET_ITEM(p, i))) {
			printf("list\n");
		} else if (PyFloat_Check(PyList_GET_ITEM(p, i))) {
			printf("float\n");
		} else if (PyLong_Check(PyList_GET_ITEM(p, i))) {
			printf("int\n");
		} else if (PyUnicode_Check(PyList_GET_ITEM(p, i))) {
			printf("str\n");
		} else {
			printf("%s\n", Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
		}
	}
}
