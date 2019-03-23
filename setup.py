from setuptools import setup

setup(
    name             = 'cini',
    version          = '0.1',
    author           = 'szsdk',
    packages         = ['.'],
    py_modules       = ['cini'],
    install_requires = [
        'Click',
    ],
    # package_data={'searchcommand': ['example_rc.py']},
    entry_points     = '''
        [console_scripts]
        cini=cini:main
    ''',
    include_package_data=True,
)
