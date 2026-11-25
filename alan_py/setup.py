from setuptools import find_packages, setup

package_name = 'alan_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Furkan Ortatepe',
    maintainer_email='furkanortatepe31@gmail.com',
    description='RectangleArea servisi sunucu ve istemci dugumleri',
    license='MIT',
    entry_points={
        'console_scripts': [
            'alan_sunucu = alan_py.alan_sunucu:main',
            'alan_istemci = alan_py.alan_istemci:main',
        ],
    },
)
