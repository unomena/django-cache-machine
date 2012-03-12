from setuptools import setup

import caching


setup(
    name='django-cache-machine',
    version='%s.unomena.3' % caching.__version__,
    description='Automatic caching and invalidation for Django models '
                'through the ORM.',
    long_description=open('README.rst').read(),
    author='Jeff Balogh',
    author_email='jbalogh@mozilla.com',
    url='http://github.com/jbalogh/django-cache-machine',
    license='BSD',
    packages=['caching', 'caching.backends'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
