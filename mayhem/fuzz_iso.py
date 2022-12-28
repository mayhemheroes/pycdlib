#!/usr/bin/env python3
import random

import atheris
import sys
import struct
import fuzz_helpers
import io

with atheris.instrument_imports(include=['pycdlib']):
    import pycdlib

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    #iso = pycdlib.PyCdlib()
    #iso.new()
    #try:
     #   with fdp.ConsumeMemoryFile() as out, io.BytesIO() as extracted:
      #      iso.open_fp(out)
       #     iso.get_file_from_iso_fp(extracted, iso_path="/" + fdp.ConsumeRemainingString())
        #    iso.close()
    #except PyCdlibInvalidInput:
     #   return -1
    try:
        bea = pycdlib.udf.BEAVolumeStructure()
        bea.parse(fdp.ConsumeRemainingBytes(), fdp.ConsumeIntInRange(0, 10))
        fp = io.BytesIO()
        pycdlib.utils.zero_pad(fp, fdp.ConsumeInt())
    except struct.error:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
