"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

"""
Takes an incoming PDU and checks its metadata for a user-defined key/value pair. 
The complete PDU is forwarded only when the metadata matches; otherwise, it is discarded.
"""

import numpy as np
from gnuradio import gr
import pmt
import sys

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, key = 'PDU', value = 1.0):  # only default arguments here
        self.key = key
        self.value = value
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='PDU Splitting',   # will show up in GRC
            in_sig=None,
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_in(pmt.intern("Input"))
        self.set_msg_handler(pmt.intern("Input"),self.add_key_value)

        self.message_port_register_out(pmt.intern("Metadata"))
        self.message_port_register_out(pmt.intern("Output"))

    def add_key_value(self,pdu):
        try:
            meta = pmt.car(pdu)
            data = pmt.cdr(pdu)
            meta = pmt.dict_add(meta,pmt.intern(self.key), pmt.from_double(self.value))
            self.message_port_pub(pmt.intern("Metadata"), meta)
            self.message_port_pub(pmt.intern("Output"), data)
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            line_number = exc_tb.tb_lineno
            print(f"Error splitting PDU: Line {line_number} : {e}")
