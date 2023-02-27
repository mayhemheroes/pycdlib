#!/usr/bin/env python3
import random

import atheris
import sys
import struct
import fuzz_helpers
import io

with atheris.instrument_imports(include=['pycdlib']):
    import pycdlib

# Exceptions
from pycdlib.pycdlibexception import PyCdlibException
iso = pycdlib.PyCdlib()
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeMemoryFile(all_data=True) as fp:
            iso.open_fp(fp)
            iso.list_children(iso_path='/')
            iso.close()
    except (PyCdlibException, struct.error, IndexError) as e:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
