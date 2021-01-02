from setuptools import setup, version

setup(
    name='websearchcli',
    author='Tsatsu Dave',
    author_email='emsonjunior@gmail.com',
    license='MIT License',
    version='0.01',
    py_modules=['webcli'],
    install_requires=['Click', 'Pyperclip'],
    entry_points='''
    [console_scripts]
    search=webcli:main
    ''',
)