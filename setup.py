from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Book Recommendation System"
AUTHOR_USER_NAME = "AYODEJI REYNOLDS OMOLUSI"
SRC_REPO = "books_recommendation"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="AYODEJI REYNOLDS OMOLUSI",
    description="A small local packages for ML based book recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Djnolds/End-to-End-Recommendation-System",
    author_email="ayodejireynolds@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)