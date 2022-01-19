    # known_ports = []
    # while not vcp.ser.isOpen():
    #     # Get all ports connected to a STM
    #     ports = vcp._search_for_board()
    #     # Check if anything changed
    #     if ports != known_ports:
    #         known_ports = ports
    #         # Try to start the hotboard
    #         if vcp.start_hot_board():
    #             break
    #         else:
    #             continue