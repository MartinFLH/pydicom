#!/usr/bin/env python

from distutils.core import setup
import os
import os.path

import sys

setup(name="pydicom",
      version="0.9.2",
      description="Pure python package for DICOM file reading and writing",
      author="Darcy Mason",
      author_email="darcymason@gmail.com",
      url="http://pydicom.googlecode.com",
      packages=['dicom'],
	  package_data={'dicom': ['examples/*', 'test/*', 'testfiles/*', 'util/*']},
      license = "Gnu General Public License",
      classifiers = [
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps."
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries",
        ]

     )

