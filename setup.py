from setuptools import setup

setup(name='helloworld',
      version='1.0.0',
      url='https://github.com/rohitkolapkar/HaloPlugin',
      license='GNU Affero General Public License v3.0',
      author='Rohit Kolapkar',
      author_email='rohitkolapkar333@gmail.com',
      description='CSM APIs Extention Demo',
      package_dir={'HelloWorld': 'HelloWorld'},
      packages=['HelloWorld', 'HelloWorld.controllers',
                'HelloWorld.services',
                'HelloWorld.commons'
                ],
      zip_safe=False,
      python_requires='>=3.6')
