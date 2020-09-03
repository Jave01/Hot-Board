# ******************************************
# file: main.py
# project: Hot-Board
# ******************************************
from vcp_handler import vcp_reader
import event_handler

s = vcp_reader(9600,'COM3')
#s.print()