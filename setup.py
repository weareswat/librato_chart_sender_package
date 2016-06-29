from setuptools import setup, find_packages

setup(name='chart_sender',
      version='0.3',
      description='Rupeals library to send Librato charts via email',
      url='https://github.com/weareswat/librato_chart_sender_package',
      author='Goncalo Correia / Pawel Krysiak / SWAT - Rupeal',
      author_email='swat@weareswat.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'jinja2',
            'requests',
            'unittest2'
      ],
      zip_safe=False,
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],)