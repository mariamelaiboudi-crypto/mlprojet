from setuptools  import setup,find_packages
from typing import List
HYPEN_E_DOT = "-e ."
def getrequirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
         requirements=  f.readlines()
         requirements=[elemet.replace('\n','') for elemet in requirements]   
         if HYPEN_E_DOT in requirements:
              requirements.remove(HYPEN_E_DOT)

              
       
print(getrequirement('requirements.txt'))
setup(
    name='projetml',
    version='0.0.1',
    author='maryam',
    packages=find_packages(),
    install_requires=getrequirement('requirements.txt')
)