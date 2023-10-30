from setuptools import find_packages, setup
from typing import List

hyphen_E_dot = '-e .'
def get_requirements(file_path: str)->List[str]:
    '''This function will return the list of requirements'''
    requiremets = []
    with open(file_path) as file_obj:
        requiremets = file_obj.readlines()
        requiremets = [req.replace('/n', '') for req in requiremets]

        if hyphen_E_dot in requiremets:
            requiremets.remove(hyphen_E_dot)

    return requiremets

setup(
    name='MLproject',
    version='0.0.1',
    author='Your name',
    author_email='Your email',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
