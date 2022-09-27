#include <pybind11/pybind11.h>

namespace py = pybind11;

py::list add(py::list l1, py::list l2) {
    py::list result(l1.size());

    if (l1.size() != l2.size())
        return result;

    for (size_t i = 0; i < l1.size(); ++i)
    {
        result[i] = l1[i] + l2[i];
    }

    return result;
}

void clip(py::list in, int min_value, int max_value) {
    size_t idx = 0;
    auto it_in = in.begin();

    for (; it_in != in.end(); ++it_in, ++idx)
    {
        const int curr_val = it_in->cast<int>();

        if (curr_val < min_value)
        {
            in[idx] = min_value;
        }
        else if (curr_val > max_value)
        {
            in[idx] = max_value;
        }
    }
}

PYBIND11_MODULE(math_cpp_python, m) {
    m.def("add", &add, "doc...");
    m.def("clip", &clip, "doc...");
}
