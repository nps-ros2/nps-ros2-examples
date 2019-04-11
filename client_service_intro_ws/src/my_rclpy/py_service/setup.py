from setuptools import setup

package_name = 'my_rclpy_my_service'

setup(
    name=package_name,
    version='0.5.1',
    packages=[],
    py_modules=[
        'service',
        'service_member_function'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Bruce Allen',
    author_email='bdallen@nps.edu',
    maintainer='Bruce Allen',
    maintainer_email='bdallen@nps.edu',
    keywords=['ROS'],
#    classifiers=[
#        'Intended Audience :: Developers',
#        'License :: OSI Approved :: Apache Software License',
#        'Programming Language :: Python',
#        'Topic :: Software Development',
#    ],
    description='Examples of minimal service servers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={'console_scripts': [
            'service = service:main',
            'service_member_function = service_member_function:main']}
)
