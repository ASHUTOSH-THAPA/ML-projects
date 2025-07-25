from setuptools import find_packages,setup
hypen='-e .'

def get_requirements(filepath:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
       requirements=file_obj.readlines()
       requirements=[req.replace("\n"," ") for req in requirements]
       if hypen in requirements:
        requirements.remove(hypen)
    return requirements    

setup(
    name='myproject',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Ashutosh Thapa',
    author_emial='ashutoshthapa2003@gmail.com',
    description='My ML project packaged for reuse',
    package=find_packages()
)