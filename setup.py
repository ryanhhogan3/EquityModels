from setuptools import setup, find_packages

setup(
    name='EquityModels',
    version='0.1',
    author='Ryan Hogan',
    author_email='ryanhhogan@gmail.com',
    description='A library containing various equity price modeling equations',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=[],
    url='',
    packages=find_packages(),
    scripts=[],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Finance'
    ],
)