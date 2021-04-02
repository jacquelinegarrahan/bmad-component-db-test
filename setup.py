from setuptools import find_packages, setup

setup(
    name='bmad-components-db-test',
    version=0,
    author='SLAC National Accelerator Laboratory',
    packages=find_packages(),
    description='Sample bmad containers',
    entry_points={
        'happi.containers': ['bmad_components = bmad_components.containers'],
    }
)