from setuptools import setup, find_packages


setup(name='global_identity',
      version='1.1.0',
      description='Global Identity Authentication PIP',
      long_description=open('README.md').read().strip(),
      author='mralves',
      author_email='mralves@stone.com.br',
      url='http://path-to-my-packagename',
      packages=find_packages(exclude=['examples', 'tests']),
      py_modules=['global_identity'],
      install_requires=[],
      license='MIT License',
      zip_safe=False,
      keywords='global identity',
      classifiers=['Authentication'])
