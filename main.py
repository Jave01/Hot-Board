# ******************************************
# file: main.py
# project: Hot-Board
# ******************************************
import vcp_handler
import event_handler

vcp = vcp_handler.vcp_reader()
print(vcp.get_available_serial_ports())

#s.print()