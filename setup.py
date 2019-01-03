from setuptools import setup, find_packages

setup(name='propygate',
      version='1.0',
      description='A simple measuremente and error propagation library',
      classifiers=[
          'Development Status : 3 - Alpha',
          'Environment :: Console',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='measurement error propagation',
      url='https://github.com/luizsol/propygate',
      author='Luiz Sol',
      author_email='luizedusol@gmail.com',
      packages=find_packages(),
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
