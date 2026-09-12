# GNU Radio PDU Utilities

Embedded Python blocks for processing Protocol Data Units (PDUs) in GNU Radio Companion.

## PDU Splitter

Takes an incoming PDU, adds a user-defined key/value pair to its metadata, and splits it across two output ports: one for the metadata dictionary and one for the data payload.

## PDU Metadata Filter

Checks an incoming PDU's metadata for a user-defined key/value pair. The complete PDU is passed to the output only when the metadata contains an exact match; otherwise, it is discarded.
