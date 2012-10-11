#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    author='KTH Infosys',
    author_email='itsc@kth.se',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
    description='CAS 2.0 authentication backend for Django',
    download_url='http://code.google.com/r/edmundcrewe-proxypatch/source',
    keywords='django cas cas2 authentication middleware backend',
    license='MIT',
    long_description="""
``django_cas`` is a `CAS` 2.0 authentication backend for
`Django`_. It allows you to use Django's built-in authentication mechanisms
and ``User`` model while adding support for CAS.

It also includes a middleware that intercepts calls to the original login and
logout pages and forwards them to the CASified versions, and adds CAS support
to the admin interface.

.. _CAS: http://www.ja-sig.org/products/cas/
.. _Django: http://www.djangoproject.com/
""",
    name='django_cas',
    packages=['django_cas'],
    url='http://code.google.com/p/django-cas/',
    version='2.0.3-KTH-11',
)
