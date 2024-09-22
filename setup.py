from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme= arq.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="imag_process",
    version="0.0.1",
    author="Loxzfusion",
    description="Pacote de processamento de imagem",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Loxzfusion/Process_imag.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires= '>=3.5',
     
)