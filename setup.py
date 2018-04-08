from setuptools import setup

requirements = [
    'click'
]

setup(
    name='cookiecutter-template',
    version='0.1.0',
    description="Template package",
    author="Kosta Zabashta",
    author_email='kosta.zabashta@gmail.com',
    url='https://github.com/kzabashta/cookiecutter-template',
    packages=['cookiecutter_template'],
    entry_points={
        'console_scripts': [
            'cookiecutter_template=cookiecutter_template.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='cookiecutter-template',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
