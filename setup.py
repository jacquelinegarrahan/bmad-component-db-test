from setuptools import find_packages, setup

import versioneer

setup(
    name='bmad_component_db',
    version=0,
    author='SLAC National Accelerator Laboratory',
    packages=find_packages(),
    description='Sample bmad containers',
    entry_points={
        'happi.containers': ['bmad_components = bmad_components.containers'],
    }
)