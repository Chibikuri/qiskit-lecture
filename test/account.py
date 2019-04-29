import sys
import Qconfig_IBMQ_experience as Qex
from qiskit import IBMQ


def check():
    try:
        IBMQ.delete_accounts()
        IBMQ.disable_accounts()
    except:
        print("disk is cleaned")
    
    try:
        IBMQ.enable_account(Qex.APItoken)
        IBMQ.save_account(Qex.APItoken, overwrite=True)
        return True
    except:
        return False