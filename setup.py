from setuptools import find_packages, setup

setup(
    name="Wafer_Fault",
    version="0.0.1",
    author="GangadharaRaviTeja",
    author_email="gangadhararaviteja092003@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)