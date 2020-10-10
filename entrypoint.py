import sys
import yaml
import os
import json
import tempfile
import subprocess
import shutil
from distutils.util import strtobool
from loguru import logger
import tempfile

from jinja2 import Environment, PackageLoader, select_autoescape




def prepare_job():
    """ Prepare temp dir"""
    dirpath = tempfile.mkdtemp()
    os.chdir(dirpath)
    template = env.get_template('templates/dataset-metadata.j2')

    env = Environment(
        loader=PackageLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    return
# Resolve if dataset has to be created

# Prepare temp dirname

# Prepare filenames

# PRepare

# prepare meta json if no

def main():
    logger.info("Start")
    for key in os.environ.keys():
        valor=os.environ[key]
        logger.debug(f"llave {key} : {valor}")
        print(os.environ.get('HOME', '/home/username/'))

    prepare_job()
    logger.info("info")
    return

if __name__ == '__main__':
    main()

    print("|||||||||||||" , dir())
    print("|||||||||||||" ,globals())
    print("|||||||||||||",locals())
    for dirname, _, filenames in os.walk('/'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
