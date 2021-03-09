from setuptools import setup


setup(
    name='packagename',
    description='Useful package',
    url='https://example.com',
    license='LICENSE',
    python_requires='>=3.6',
    packages=['packagename'],
    install_requires=['pytest'],
    entry_points={'console_scripts':['packagename=packagename.packagename:main']},
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'])
