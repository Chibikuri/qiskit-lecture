import sys
import account
import qiskit

version = sys.version_info

if version[0] != 3 or not qiskit.__version__.startswith("0.8"):
    raise Warning("My program may not work properly.")

if version[3] != 'final':
    print("Reccomend: upgrade python")

if not account.check():
    raise Exception("Invalid account. Check Qconfig_IBMQ_Experience.py")
else:
    print("Enjoy python and qiskit!")