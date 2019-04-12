#!/usr/bin/env python

from setuptools import setup

setup(name='PythonSequenceFile',
      version='0.0.1',
      description='Python Hadoop Sequence File Utilities',
      license="Apache Software License 2.0 (ASF)",
      author='Matteo Bertozzi',
      author_email='theo.bertozzi@gmail.com',
      url='http://hadoop.apache.org',
      packages=["hadoop", 'hadoop.util', 'hadoop.io', 'hadoop.io.compress'],
      extras_require = {
        'pydoop': ['pydoop>=0.9.1']
        }
     )

