from setuptools import setup,find_packages

# setup(
#     name='hello',
#     version=0.1,
#     py_modules=['hello'],
#     install_requires=['Click',],
#     entry_points='''
#         [console_scripts]
#         hello=hello:cli
#     ''',
#
# )

setup(
    name='myapp',
    version='0.1',
    description='myapp',
    author='pitt.liu',
    url='',
    license='',
    packages=find_packages(),
    #scripts=['myapp/hello.py'],
    entry_points=
    {'console_scripts':['hello=myapp.hello:main']}
)