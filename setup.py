#make sure you make any necassary changes before running this
from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()

with open ('readme.md') as f:
    long_description = f.read()

#print(long_description)



setup(
        name ='dlc_control',
        version ='1.0.0',
        author ='Andreas Svela',
        maintainer='Tim Newman',
        maintainer_email='timothy.newman@sydney.edu.au',
        url ='https://github.com/Quantum-Integration-Laboratory/dlc_control',
        description ='QIL Fork of wrapper of Toptica Laser SDK for controlling a Toptica CTL with a DLCpro',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        keywords ='laser',
        install_requires = requirements,
        zip_safe = False
)