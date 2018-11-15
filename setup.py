# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='lesscache',
    version='0.1',
    url='http://github.com/ebertti/lesscache/',
    author='Estante Virtual',
    author_email='ebertti@gmail.com',
    install_requires=['boto3',],
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    license='MIT License',
    platforms=['OS Independent'],
    description='AWS Dynamodb as cache backend for Django and Flask',
    long_description=(open('README.rst').read()),
    keywords=['cache', 'django', 'flask', 'aws', 'dynamodb'],
    test_suite='pytest',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
)
