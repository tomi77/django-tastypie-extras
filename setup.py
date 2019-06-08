from codecs import open

from setuptools import setup, find_packages

setup(
    name="django-tastypie-extras",
    version='0.4b1',
    author='Tomasz Jakub Rup',
    author_email='tomasz.rup@gmail.com',
    url='https://github.com/tomi77/django-tastypie-extras',
    description='A set of Django tastypie extras (Multipart resource, smart paginator, SwaggerUI authentication, CSV serializer)',
    long_description=open("README.rst").read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'django-extras'
    ],
    extras_require={
        'csv': ['unicodecsv'],
    }
)
