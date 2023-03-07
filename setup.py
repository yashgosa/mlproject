from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    """
    Reads the requirements.txt file and returns a list of strings.
    :param file_path: Path to the requirements.txt file.
    :return: List of strings.
    """

    with open(file_path) as f:
        requirements = f.readlines()
        [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    version='0.0.1',
    description='A short description of the project.',
    author='Yash Gosavi',
    author_email='yashcgosvai@gmail.com',
    license='MIT'
    )
    
            
    