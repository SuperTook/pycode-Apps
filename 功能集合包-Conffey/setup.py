from setuptools import setup
from conffey import __version__


def read_requirements(filename):
    res = []
    for line in open(filename).read().splitlines():
        if not line.startswith('#'):
            res.append(line.strip())
    return res


setup(
    name='conffey',
    version=__version__,
    description=(
        'A library that encapsulates various functions of Python.'
    ),
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='C.Z.F.',
    author_email='3023639843@qq.com',
    maintainer='C.Z.F.',
    maintainer_email='3023639843@qq.com',
    license='BSD License',
    packages=['conffey'],
    python_requires='>=3.6.0',
    install_requires=read_requirements('requirements.txt'),
    platforms=['all'],
    url='https://github.com/super-took/conffey',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ]
)
