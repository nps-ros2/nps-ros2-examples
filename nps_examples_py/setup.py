from setuptools import find_packages
from setuptools import setup

package_name = 'nps_examples_py'

setup(
    name=package_name,
    version='0.6.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='your name',
    author_email='you@yours.com',
    maintainer='your name',
    maintainer_email='you@yours.com',
    keywords=['ROS'],
    classifiers=[
        'Programming Language :: Python'
    ],
    description=(
        'Adapted from ROS2 demos.'
    ),
    license='your license',
    entry_points={
        'console_scripts': [
            'listener = nps_examples_py.topics.listener:main',
            'talker = nps_examples_py.topics.talker:main'
        ],
    },
)
