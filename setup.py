#!/usr/bin/env python

import sys
import os, errno
import shlex
import subprocess as sp
import argparse

"""
Setup script. Initialises:
    - the payu lab (which includes work, archive and source code directories.)
    - standard experiments.
    - standard model input.
"""

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--download_input_data", action='store_true',
                        default=False, help="""
                        Download experiment input data.""")

    args = parser.parse_args()

    mkdir_p('lab/archive')
    mkdir_p('lab/bin')
    mkdir_p('lab/codebase')

    # Download input data.
    data = '/short/public/access-om/access-om.tar.gz'
    if args.download_input_data:
        # FIXME: download from Ramadda.
        # data = ''
        pass

    if not os.path.exists('lab/input'):
        cwd = os.getcwd()
        try:
            os.chdir('lab')
            cmd = '/bin/tar -zxvf {}'.format(data)
            ret = sp.call(shlex.split(cmd))
        finally:
            os.chdir(cwd)

        assert(ret == 0)

    return 0

if __name__ == '__main__':
    sys.exit(main())