from setuptools import setup, find_packages

REQUIRES = [
    'click',
    'Kivy',
    'ruamel.yaml'
]

setup(
    name='humankind-unfolding',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',

    install_requires=REQUIRES,

    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={  #
        'humankind-unfolding': ['data/goals.yaml'],
    }
)
