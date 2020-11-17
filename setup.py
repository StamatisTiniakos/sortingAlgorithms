from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open('requirements.txt') as f:
    requires = tuple(l[:-1] for l in f)

setup(
    name="sortingAlgorithms", # Replace with your own username
    version="1.0.0",
    #install_requires = ['requests']
    install_requires=requires,
    author="Stamatis Tiniakos",
    author_email="stam.tiniakos@gmail.com",
    description="Python array sorting Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StamatisTiniakos/sortingAlgorithms/",
    download_url = 'https://github.com/StamatisTiniakos/sortingAlgorithms/archive/main.zip'
    #packages=['sortingAlgorithms'],
    packages = find_packages(exclude=['tests*']),
    keywords = ['sorting','algorithm','python'],
    include_package_data=True,
    license = 'MIT License: http://opensource.org/licenses/MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)