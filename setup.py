import sys
import setuptools
import os
from pip.req import parse_requirements
# noinspection PyProtectedMember
from pip.download import PipSession

VERSION = open(os.path.join('angreal', 'VERSION')).read().strip()
py_version_tag = '-%s.%s'.format(sys.version_info[:2])

if not sys.version_info >= (3, 0):
    print('Python 3 is required', file=sys.stderr)
    exit(1)


def read_requirements(f):
    """
    Get requirements from a requirements file, will follow links.
    :param f:
    :return:
    """

    install_reqs = parse_requirements(f, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs


setuptools.setup(
    name='angreal',
    description='making data science projects portable and consistent',
    long_description='''
    ''',
    url='https://gitlab.com/dylanbstorey/angreal',
    author='dylanbstorey',
    author_email='dylan.storey@gmail.com',
    license='GPLv3',
    packages=setuptools.find_packages(),
    install_requires=read_requirements('requirements/requirements.txt'),
    zip_safe=False,
    version=VERSION,
    entry_points={
        'console_scripts': [
            'angreal = angreal.main:main'
        ]
    },
    python_requires='>=3.6',
    include_pacakge_data=True,
    tests_require=['nose'],
    test_suite='nose.collector',
    extras_requires={
        'dev': read_requirements('requirements/dev.txt')
    }
)
