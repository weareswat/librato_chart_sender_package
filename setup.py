from setuptools import setup

setup(name='librato_chart_sender',
      version='0.1',
      description='Rupeals library to send Librato charts via email',
      url='https://github.com/weareswat/librato-chart-sender',
      author='Goncalo Correia / Pawel Krysiak / SWAT - Rupeal',
      author_email='swat@weareswat.com',
      license='MIT',
      packages=['librato_chart_sender'],
      install_requires=[
            'jinja2',
            'requests',
            'json'
      ],
      # dependency_links=[
      #     'https://github.com/weareswat/librato-chart-sender'
      # ],
      zip_safe=False,
      include_package_data=True)