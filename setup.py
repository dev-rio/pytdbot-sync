from re import findall
from setuptools import setup, find_packages


with open("pytdbot_sync/__init__.py", "r") as f:
    version = findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", "r") as f:
    readme = f.read()

with open("requirements.txt", "r") as f:
    requirements = [x.strip() for x in f.readlines()]


setup(
    name="Pytdbot-sync",
    version=version,
    description="Easy-to-use synchronous TDLib wrapper for Python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="AYMEN Mohammed",
    author_email="let.me.code.safe@gmail.com",
    url="https://github.com/dev-rio/pytdbot-sync",
    license="MIT",
    python_requires=">=3.9",
    install_requires=requirements,
    project_urls={
        "Source": "https://github.com/dev-rio/pytdbot-sync",
        "Tracker": "https://github.com/dev-rio/pytdbot-sync/issues",
    },
    packages=find_packages(exclude=["examples"]),
    package_data={
        "pytdbot-sync": ["lib/*.so", "td_api.*"],
    },
    keywords=[
        "telegram",
        "tdlib",
        "bot",
        "telegram-client",
        "telegram-bot",
        "bot-api",
        "telegram-bot",
        "tdlib-python",
        "tdlib-bot",
    ],
)
