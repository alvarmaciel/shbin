from setuptools import setup, find_packages

setup(
    name='shbin',
    version='0.3.1',
    packages=find_packages(),  # This will automatically find packages, but since shbin is a script, no packages are defined yet
    py_modules=['shbin'],  # This tells setuptools to include shbin.py as a module
    entry_points={
        'console_scripts': [
            'shbin = shbin:main',  # This assumes that shbin.py has a function called main() which is the entry point of your CLI
        ],
    },
    include_package_data=True,  # This tells setuptools to include non-python files from MANIFEST.in
    # Optional metadata to include
    author='Alvar Maciel, Martín Gaitan',
    author_email='alvarmaciel@gmail.com',
    description='Turns a Github repo into a pastebin ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT License',
    url='https://github.com/alvarmaciel/shbin',
    classifiers=[  # Classifiers help users find your project by categorizing it.
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
