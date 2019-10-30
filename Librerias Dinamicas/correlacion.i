%module correlacion

%{
    #define SWIG_FILE_WITH_INIT
    #include "correlacion.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (int* IN_ARRAY1, int DIM1){(int* X, int n),(int* Y, int m)}

%include "correlacion.h"
