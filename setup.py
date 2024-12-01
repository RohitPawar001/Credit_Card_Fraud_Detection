from setuptools import find_package, set_up
from typing import List

HYPEN_E_DOT = "-e."
def get_requirements(file_path:str) -> list[str]:
    requirements = []
    with open(file_path,"r") as file_obj:
        requirement = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirement]
        
    if HYPEN_EDOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements
         

setup(
    name = "Credit_card_Fraud_detection",
    version = "0.0.1",
    author = "Rohit Pawar",
    auther_email = "rppawar491@gmail.com",
    packages = find_packages(),
    install_requireents = get_requirements("requirements.txt")
)
