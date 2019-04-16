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
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'Adapted from ROS2 demos.'
    ),
    license='Apache License, Version 2.0',
    entry_points={
        'console_scripts': [
            'listener = nps_examples_py.topics.listener:main',
            'talker = nps_examples_py.topics.talker:main'
        ],
    },
)
