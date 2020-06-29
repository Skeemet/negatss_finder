# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable
import requests.certs


executable = Executable( script = "negatss_finder.py", base = "Win32GUI" )

# Add certificate to the build
options = {
"build_exe": {
"include_files" : [(requests.certs.where(), "cacert.pem")],
"includes":["idna.idnadata"]
}
}

setup(
    name = "Algorithm",
    version = "3.1",
    description = "Algorithm help tool.",
    requires = ["requests"],
    options = options,
    executables = [executable] )