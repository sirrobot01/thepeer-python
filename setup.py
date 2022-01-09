from setuptools import setup, find_packages

def read(f):
    return open(f, 'r', encoding='utf-8').read()


setup(
    name="thepeer",
    version='0.0.1',
    description="The Peer unofficial SDK",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url="https://github.com/sirrobot01/thepeer-python",
    author="Mukhtar Akere",
    author_email="akeremukhtar10@gmail.com",
    license="BSD-3-Clause",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        'requests'
    ],
    packages=find_packages(),
    extras_require={
        'test': ['pytest']
    },
    project_urls={
        'Source': 'https://github.com/sirrobot01/thepeer-python',
    },
)
