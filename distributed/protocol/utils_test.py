from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy


def get_host_array(a: numpy.ndarray) -> numpy.ndarray:
    """Given a numpy array, find the underlying memory allocated by either
    distributed.protocol.utils.host_array or internally by numpy
    """
    import numpy

    assert isinstance(a, numpy.ndarray)
    o: object = a
    while True:
        if isinstance(o, memoryview):
            o = o.obj
        elif isinstance(o, numpy.ndarray):
            if o.base is not None:
                o = o.base
            else:
                return o
        else:
            # distributed.comm.utils.host_array() uses numpy.empty()
            raise TypeError(
                "Array uses a buffer allocated neither internally nor by host_array: "
                f"{type(o)}"
            )
