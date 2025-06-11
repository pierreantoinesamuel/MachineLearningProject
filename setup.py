from setuptools import setup, find_packages

HYPEHINT_E_DOT = "-e ."  # Hypothetical package for type hints, adjust as needed

def read_requirements(filename="requirements.txt"):
    with open(filename, "r") as f:
        if HYPEHINT_E_DOT in f:
            f.remove(HYPEHINT_E_DOT)
        return [line.strip() and line.replace("\n"," ") for line in f if line.strip() and not line.startswith("#")]
        if HYPEHINT_E_DOT in f:
            f.remove(HYPEHINT_E_DOT)

             
    

setup(
    name="MachineLearningProject",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    author="Pierre Antoine Samuel",
    description="A machine learning project package.",
    python_requires=">=3.7",
)