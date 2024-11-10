from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # 如果有依赖项，列在这里
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',  # 假设你在 math_quiz.py 中有一个名为 main 的函数
        ],
    },
)
