from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "PROJECT.md").read_text()

setup(
    name='streamlit-mpl-svg',
    version='0.1.1',
    author='Anas Bouzid',
    author_email='anasbouzid@gmail.com',
    description='Reformat Matplotlib SVGs for easier access and customzation with CSS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/bouzidanas/streamlit-mpl-svg",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "matplotlib >= 3.2.1",
        "mpl-svg >= 0.1.4",
    ],
)