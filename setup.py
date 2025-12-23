from setuptools import setup,find_packages
from typing import List

hupy_e_dot = '-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    if hupy_e_dot in requirements:
        requirements.remove(hupy_e_dot)
    return requirements

setup(
    name='mlproject-1',
    version= '0.0.1',
    author='akash',
    author_email='akashrangarej12@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)