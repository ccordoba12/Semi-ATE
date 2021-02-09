from ATE.data.STDF import STDR


class DTR(STDR):
    def __init__(self, version=None, endian=None, record=None):
        self.id = "DTR"
        self.local_debug = False
        # Version
        if version == None or version == "V4" or version == "V3":
            if version == None:
                self.version = "V4"
            else:
                self.version = version
            self.info = """
Datalog Text Record
-------------------

Function:
    Contains text information that is to be included in the datalog printout. DTRs may be
    written under the control of a job plan: for example, to highlight unexpected test
    results. They may also be generated by the tester executive software: for example, to
    indicate that the datalog sampling rate has changed. DTRs are placed as comments in
    the datalog listing.

Frequency:
    * Optional, a test data file may contain any number of DTRs.

Location:
    Anywhere in the data stream after the initial "FAR-(ATRs)-MIR-(RDR)-(SDRs)" sequence.
"""
            self.fields = {
                "REC_LEN": {
                    "#": 0,
                    "Type": "U*2",
                    "Ref": None,
                    "Value": None,
                    "Text": "Bytes of data following header        ",
                    "Missing": None,
                },
                "REC_TYP": {
                    "#": 1,
                    "Type": "U*1",
                    "Ref": None,
                    "Value": 50,
                    "Text": "Record type                           ",
                    "Missing": None,
                },
                "REC_SUB": {
                    "#": 2,
                    "Type": "U*1",
                    "Ref": None,
                    "Value": 30,
                    "Text": "Record sub-type                       ",
                    "Missing": None,
                },
                "TEXT_DAT": {
                    "#": 3,
                    "Type": "C*n",
                    "Ref": None,
                    "Value": None,
                    "Text": "Message                               ",
                    "Missing": "",
                },
            }
        else:
            raise STDFError(
                "%s object creation error: unsupported version '%s'"
                % (self.id, version)
            )
        self._default_init(endian, record)
