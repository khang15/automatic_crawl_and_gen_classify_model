import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crawl_and_gen_model",
    version="0.0.1",
    author="Khang Nguyen An",
    author_email="nguyenankhang1505@gmail.com",
    description="Automatic crawl and generate classify model for real-estate web domain",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/khang15/automatic_crawl_and_gen_classify_model.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)