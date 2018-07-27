import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'fitness-tools',
    packages = setuptools.find_packages(),
    version = '0.1.0',  # Ideally should be same as your GitHub release tag varsion
    description = 'Healthy Lifestyles With Python',
    long_description = long_description,
    author = 'Maverick Coders',
    author_email = 'maverickcoders@pm.me',
    url = 'https://github.com/Maverick-Coders/Fitness-Tools',
    keywords = ['health', 'wellness', 'fitness', 'exercise', 'nutrition'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
