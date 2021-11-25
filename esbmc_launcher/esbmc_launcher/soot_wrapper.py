"""Converts java/kotlin/apk into a jimple file"""

from esbmc_launcher.jimple_to_json import StubConverter
import utils
from subprocess import run
import printable

class SootWrapper:

    def __init__(self, soot="soot.jar"):
        self.soot = soot


    def _compile_java_file(self, files):
        javac = utils.is_available("javac")
        if not javac:
            raise ValueError("Expecting javac in path")

        input = [javac]
        for x in files:
            input.append(x)
        printable.debug(f"Javac: {input}")
        run(input)

    def _extract_jimple(self, files):
        java = utils.is_available("java")
        if not java:
            raise ValueError("Expecting java in path")

        input = [java, "-cp", "../data/soot.jar", "soot.Main", "-cp", ".", "-pp", "-f", "jimple"]
        for x in files:
            import os
            absolute = os.path.abspath(x)
            filename = os.path.basename(absolute)
            input.append(os.path.splitext(filename)[0] + "Kt")
        printable.debug(f"Soot: {input}")
        run(input, cwd="../data")

    def generate_jimple(self, files):
        # TODO: This will be put into the tmp dir
        printable.status(f"Generating Jimple from: {files}")
        self._compile_kotlin_file(files)
        self._extract_jimple(files)
        for x in files:
            StubConverter().generate_json(x, x)


    def _compile_kotlin_file(self, files):
        kotlinc = utils.is_available("kotlinc")
        if not kotlinc:
            raise ValueError("Expecting kotlinc in path")

        input = [kotlinc, "-include-runtime"]
        for x in files:
            input.append(x)

        input.append("-d")
        input.append("output.jar")
        printable.debug(f"kotlinc: {input}")
        run(input)

        jar = utils.is_available("jar")
        if not jar:
            raise ValueError("Expecting jar in path")

        input = [jar, "xf", "output.jar"]
        run(input)
        
    
    @staticmethod
    def check_requirements(is_warning=True):
        SootWrapper.check_javac(is_warning)
        SootWrapper.check_kolinc(is_warning)
        SootWrapper.check_java(is_warning)


    @staticmethod
    def check_javac(just_warning: bool) -> bool:
        warning = printable.warning if just_warning else printable.error
        if utils.is_available("javac"):
            printable.status("Found javac, support for .java files is OK")
            return True
        else:
            warning("Couldn't find javac, .java files are disabled")
            return False

    @staticmethod
    def check_kolinc(just_warning: bool) -> bool:
        warning = printable.warning if just_warning else printable.error
        if utils.is_available("kotlinc"):
            printable.status("Found kotlinc, support for .kt files is OK")
            return True
        else:
            warning("Couldn't find kotlinc, .kt files are disabled")
            return False

    @staticmethod
    def check_java(just_warning: bool) -> bool:
        warning = printable.warning if just_warning else printable.error
        if utils.is_available("java"):
            printable.status("Found java")
            return True
        else:
            warning("Couldn't find java, this is required for Soot")
            return False

    @staticmethod
    def get_soot_link() -> str:
        return "https://repo1.maven.org/maven2/org/soot-oss/soot/4.2.1/soot-4.2.1-jar-with-dependencies.jar"
