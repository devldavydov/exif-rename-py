import setuptools


setuptools.setup(
    name='exif-rename-py',
    version='1.0',
    description='JPG rename tool by EXIF DateTimeOriginal',
    author='github.com/devldavydov',
    packages=setuptools.find_packages(where='source'),
    package_dir={'': 'source'},
    include_package_data=True,
    install_requires=[
        'Pillow==9.1.0'
    ],
    entry_points={'console_scripts': ['exif-rename-py=exif_rename_py.__main__:main']},
    python_requires=">=3.6"
)
