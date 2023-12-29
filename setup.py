from setuptools import setup, find_packages

setup(
    name='galytix_assignment_de',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'gensim',
    ],
    entry_points={
        'console_scripts': [
            'init_pipeline = galytix_assignment_de.init_pipeline:main',
            'process_data = galytix_assignment_de.process_data:main',
        ],
    },
)
