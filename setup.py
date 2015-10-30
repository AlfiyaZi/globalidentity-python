import setuptools
from global_identity.version import Version


setuptools.setup(name='global_identity',
                 version=Version('1.0.0').number,
                 description='Global Identity Authentication PIP',
                 long_description=open('README.md').read().strip(),
                 author='mralves',
                 author_email='mralves@stone.com.br',
                 url='http://path-to-my-packagename',
                 py_modules=['global_identity'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='global identity',
                 classifiers=['Authentication'])
