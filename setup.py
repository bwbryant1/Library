from setuptools import setup

setup(name='Library',
      version='0.1',
      description='A simple library application',
      url='http://github.com/bwbryant1/Library',
      author='Team Fuschia',
      author_email='bwb016@email.latech.edu',
      license='MIT',
      packages=['library'],
      install_requires=[
          'sqlite3',
      ],
      zip_safe=False)
