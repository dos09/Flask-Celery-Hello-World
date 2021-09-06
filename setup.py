from setuptools import find_packages, setup

REQUIRES = (
    'celery==5.1.2',
    'Flask==2.0.1',
    'gunicorn==20.1.0',
    'redis==3.5.3'
)

if __name__ == '__main__':
    setup(
        name='hello-world',
        version='0.0.0',
        packages=find_packages(include=[
            'entry_apps*',
            'hello_world*'
        ]),
        platforms=('any',),
        install_requires=REQUIRES
    )
