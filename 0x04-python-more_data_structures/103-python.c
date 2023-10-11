#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - function name
 * @p: the fisrt input
 */
void print_python_bytes(PyObject *p)
{
	long int j = 0, L;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)(p))->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (((PyVarObject *)(p))->ob_size < 10)
		L = ((PyVarObject *)(p))->ob_size + 1;
	else
		L = 10;

	printf("  first %ld bytes:", L);

	while (j < L)
	{
		if (((PyBytesObject *)p)->ob_sval[j] < 0)
			printf(" %02x", 256 + ((PyBytesObject *)p)->ob_sval[j]);
		else
			printf(" %02x", ((PyBytesObject *)p)->ob_sval[j]);
		j++;
	}
	printf("\n");
}

/**
 * print_python_list - The function name
 * @p: the input of the function
 */
void print_python_list(PyObject *p)
{
	PyObject *object;
	long int S, j;

	S = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", S);
	printf("[*] Allocated = %ld\n", (PyListObject *)p->allocated);

	j = 0;
	while (j < S)
	{
		object = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
		j++;
	}
