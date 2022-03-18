import pybase64

sampleBytes = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")

_base64 = pybase64.b64encode(sampleBytes)

print(_base64)