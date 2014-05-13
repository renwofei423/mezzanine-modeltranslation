from setuptools import setup

setup(
    name='mezzaninemodeltranslation',
    version='0.1',
    description='Integrate Mezzanine and django-modeltranslation',
    long_description=open('README.md').read(),
    author='Roman Medvedev',
    url='http://github.com/Romamo/mezzanine-modeltranslation',
    license='BSD',
    packages=('mezzaninemodeltranslation',),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)