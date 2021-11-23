"""Converts java/kotlin/apk into a jimple file"""

import utils
from subprocess import run
from printable import Message

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
        Message.debug(f"Javac: {input}")
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
            input.append(os.path.splitext(filename)[0])
        Message.debug(f"Soot: {input}")
        run(input, cwd="../data")

    def generate_jimple(self, files):
        # TODO: This will be put into the tmp dir
        Message.status(f"Generating Jimple from: {files}")
        self._compile_java_file(files)
        self._extract_jimple(files)


    @staticmethod
    def check_requirements(is_warning=True):
        SootWrapper.check_javac(is_warning)
        SootWrapper.check_kolinc(is_warning)
        SootWrapper.check_java(is_warning)


    @staticmethod
    def check_javac(just_warning: bool) -> bool:
        warning = Message.warning if just_warning else Message.error
        if utils.is_available("javac"):
            Message.status("Found javac, support for .java files is OK")
            return True
        else:
            warning("Couldn't find javac, .java files are disabled")
            return False

    @staticmethod
    def check_kolinc(just_warning: bool) -> bool:
        warning = Message.warning if just_warning else Message.error
        if utils.is_available("kotlinc"):
            Message.status("Found kotlinc, support for .kt files is OK")
            return True
        else:
            warning("Couldn't find kotlinc, .kt files are disabled")
            return False

    @staticmethod
    def check_java(just_warning: bool) -> bool:
        warning = Message.warning if just_warning else Message.error
        if utils.is_available("java"):
            Message.status("Found java")
            return True
        else:
            warning("Couldn't find java, this is required for Soot")
            return False

    @staticmethod
    def get_soot_link() -> str:
        return "https://repo1.maven.org/maven2/org/soot-oss/soot/4.2.1/soot-4.2.1-jar-with-dependencies.jar"
