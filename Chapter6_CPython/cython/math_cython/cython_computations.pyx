cimport cython


ctypedef fused vector_type:
    float
    double


def _naive_cython_clip_vector(
    list_in,
    min_value,
    max_value,
    list_out
):
    for idx in range(len(list_in)):
        list_out[idx] = min(max(list_in[idx], min_value), max_value)


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)  # Deactivate negative indexing
def _cython_clip_vector(
    vector_type[:] list_in,
    vector_type min_value,
    vector_type max_value,
    vector_type[:] list_out
):
    for idx in range(len(list_in)):
        list_out[idx] = min(max(list_in[idx], min_value), max_value)


from cython.parallel import prange


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)  # Deactivate negative indexing
def _cython_clip_vector_parallel(
    vector_type[:] list_in,
    vector_type min_value,
    vector_type max_value,
    vector_type[:] list_out
):
    cdef signed int idx = 0
    cdef signed int length = len(list_in)
    with nogil:
        for idx in prange(length, schedule="guided"):
            if list_in[idx] < min_value:
                list_out[idx] = min_value
            if list_in[idx] > max_value:
                list_out[idx] = max_value
