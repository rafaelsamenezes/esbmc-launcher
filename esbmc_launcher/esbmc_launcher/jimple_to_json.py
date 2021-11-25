"""Converts .jimple into a json to be later used by ESBMC"""

import printable

class JimpleToJson:
    """Jimple convertion methods"""

    def generate_json(self, origin: str, destiny: str):
        """From a Jimple file <origin> generates the AST and
           save it into <destiny> """
        pass

class StubConverter(JimpleToJson):

    def generate_json(self, origin: str, destiny: str):
        """Lets pretend that a conversion happened"""
        printable.status(f"Generating AST from Jimple file: {origin}")
