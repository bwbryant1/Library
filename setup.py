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
          'pyqt5',
      ],
      classifiers=[
          'Programming Language :: Python :: 3',
      ],
      package_data = {'library':['icons/*svg']},
      entry_points={'console_scripts': ['libraryman = library.core:main','libraryman-cli = library.cli:main']},
      zip_safe=False)
