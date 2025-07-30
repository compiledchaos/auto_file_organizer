from setuptools import setup, find_packages

setup(
    name="auto_file_organizer",
    version="0.1.0",
    description="A utility to auto-organize your files based on custom rules",
    author="Sachin Karthikeyan",
    author_email="sachinprathik8@gmail.com",
    url="https://github.com/compiledchaos/auto_file_organizer",
    packages=find_packages(),  # Finds `organizer` and submodules
    install_requires=["watchdog"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "auto-organize = runner:main",  # command -> function
        ],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
