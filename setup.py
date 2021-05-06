from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    # none :)
]

setup(
    name="slownumget",
    version="0.0.1",
    author="John Wilson",
    author_email="john4.wilson6@protonmail.ch",
    description="A package to output numbers really flipping slowly.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/your_package/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
