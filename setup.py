#!/usr/bin/env python

# Installation script for diffpy.srreal

"""diffpy.srreal - prototype for new PDF calculator and assortment
of real space utilities.

Packages:   diffpy.srreal
Scripts:    (none yet)
"""

import os
import glob
from setuptools import setup, find_packages
from setuptools import Extension
from numpy.distutils.misc_util import get_numpy_include_dirs

# define extensions here
ext_kws = {
        'libraries' : ['diffpy'],
        'extra_compile_args' : [],
        'extra_link_args' : [],
        'include_dirs' : get_numpy_include_dirs(),
}

srreal_ext = Extension('diffpy.srreal.srreal_ext',
    glob.glob('srrealmodule/*.cpp'),
    **ext_kws)


# versioncfgfile holds version data for git commit hash and date.
# It must reside in the same directory as version.py.
versioncfgfile = 'diffpy/srreal/version.cfg'

def gitinfo():
    from subprocess import Popen, PIPE
    proc = Popen(['git', 'describe'], stdout=PIPE)
    desc = proc.stdout.read()
    proc = Popen(['git', 'log', '-1', '--format=%H %ai'], stdout=PIPE)
    glog = proc.stdout.read()
    rv = {}
    rv['version'] = '-'.join(desc.strip().split('-')[:2])
    rv['commit'], rv['date'] = glog.strip().split(None, 1)
    return rv


def getversioncfg():
    import os
    from ConfigParser import SafeConfigParser
    cp = SafeConfigParser()
    cp.read(versioncfgfile)
    if not os.path.isdir('.git'):  return cp
    d = cp.defaults()
    g = gitinfo()
    if g['commit'] != d.get('commit'):
        cp.set('DEFAULT', 'version', g['version'])
        cp.set('DEFAULT', 'commit', g['commit'])
        cp.set('DEFAULT', 'date', g['date'])
        cp.write(open(versioncfgfile, 'w'))
    return cp

cp = getversioncfg()

# define distribution
setup(
        name = "diffpy.srreal",
        version = cp.get('DEFAULT', 'version'),
        namespace_packages = ['diffpy'],
        packages = find_packages(),
        test_suite = 'diffpy.srreal.tests',
        include_package_data = True,
        ext_modules = [srreal_ext],
        install_requires = [
            'diffpy.Structure',
        ],
        dependency_links = [
            # REMOVE dev.danse.us for a public release.
            'http://dev.danse.us/packages/',
            "http://www.diffpy.org/packages/",
        ],
        zip_safe = False,

        author = "Simon J.L. Billinge",
        author_email = "sb2896@columbia.edu",
        description = "Prototype for new PDF calculator and other real " + \
                      "space utilities.",
        license = "BSD",
        url = "http://www.diffpy.org/",
        keywords = "PDF calculator real-space utilities",
)

# End of file
