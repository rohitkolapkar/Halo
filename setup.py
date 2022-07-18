from setuptools import setup

setup(name='Halo',
      version='1.0.0',
      url='https://github.com/rohitkolapkar/HaloPlugin',
      license='GNU Affero General Public License v3.0',
      author='Rohit Kolapkar',
      author_email='rohitkolapkar333@gmail.com',
      description='Halo Management Plugin',
      package_dir={'halo': 'halo'},
      packages=['halo', 'halo.controllers',
                'halo.services'
                ],
      zip_safe=False,
      python_requires='>=3.6')
