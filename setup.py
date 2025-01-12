import setuptools

setuptools.setup(
    name="monterey",
    version="0.0.14",
    author="Hammad Saeed",
    author_email="hammad@supportvectors.com",
    description="monterey tools",
    long_description="""
Monterey Tools
    """,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.8',
    install_requires=[
"art",
"customtkinter",
"fire",
"prompt_toolkit",
"pathlib",
"pillow",
"rich-cli",
    ],
)