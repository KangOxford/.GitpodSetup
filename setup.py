from setuptools import find_packages, setup
from setuptools.command.install import install

setup(
    cmdclass={"install": InstallCommand},
    name="gym_exchange",
    use_scm_version={"local_scheme": get_local_version, "version_scheme": get_version},
    setup_requires=["setuptools_scm"],
    description="Implementation of modern reward and gym_exchange learning algorithms.",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="Center for Human-Compatible AI and Google",
    python_requires=">=3.8.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    extras_require={
        # recommended packages for development
        "dev": [
            "autopep8",
            "ipdb",
            "isort~=5.0",
            "codespell",
            "sphinx-autobuild",
            "sphinx~=5.1.1",
            "sphinx-autodoc-typehints~=1.19.1",
            "sphinx-rtd-theme~=1.0.0",
            "sphinxcontrib-napoleon==0.7",
            "furo==2022.6.21",
            "sphinx-copybutton==0.5.0",
            "sphinx-github-changelog~=1.2.0",
            "myst-nb==0.16.0",
            "ipykernel~=6.15.2",
        ]
    },

)
