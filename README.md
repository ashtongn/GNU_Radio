# GNU Radio Custom Blocks

Embedded Python blocks for GNU Radio Companion, organized by domain.

## PDU Utilities

### PDU Splitter

Takes an incoming PDU, adds a user-defined key/value pair to its metadata, and splits it across two output ports: one for the metadata dictionary and one for the data payload.

### PDU Metadata Filter

Checks an incoming PDU's metadata for a user-defined key/value pair. The complete PDU is passed to the output only when the metadata contains an exact match; otherwise, it is discarded.

## Streaming

### Float To Complex

Combines two `float32` streams into a single `complex64` stream. Input port 0 becomes the real (I) component and port 1 becomes the imaginary (Q) component of each output sample.

### Decimator

Decimates an incoming stream by a user-defined integer factor `N`, keeping every Nth sample. Sample type is user-selectable (`float` or `complex`) so the same block can be used on real or complex signals.
