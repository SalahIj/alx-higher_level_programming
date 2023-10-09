#include <Python.h>

/**
 * print_python_list_info -  the function name.
 * @p: the input of the function
 */

void print_python_list_info(PyObject *p)
{
	int s, allocation, j = 0;
	Pyobject *ject;

	allocation = ((PylistObject *)p)->allocated;
	s = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", allocation);

	while (j < s)
	{
		printf("Element %d: ", j);
		ject = PyList_GetItem(p, j);
		printf("%s\n", (*Py_TYPE(ject)).tp_name);
		j++;
	}
}
