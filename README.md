# Leeroo Client

<img alt="Leeroo logo" src="https://github.com/Leeroo-AI/mergoo/blob/main/static/logo.png?raw=true" width="148" align="right" />

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-green.svg)](#python)
[![Version](https://img.shields.io/pypi/v/mergoo?color=blue)](https://pypi.org/project/leeroo-client/)


**Leeroo** enables the development of the highest quality customized AI models by automating experimentation in model building. By simply defining your evaluation criteria and providing seed data, Leeroo suggests model building experiments using state-of-the-art technologies. It automates the model-building workflow, from data generation to training and evaluation. Leeroo _ensures_ the delivery of the best customized model for your use case. Moreover, model deployment is streamlined and can be achieved with a single command.

## Installation

### Install using pip

```sh
pip install leeroo-client
```

### Install from Source

```sh
git clone https://github.com/Leeroo-AI/leeroo-client
cd leeroo-client
pip install -e .
```

## Features

**High-Quality Data Generation**    
Our data generation pipeline employs compound systems, integrating the knowledge of multiple agents and tools to create high-quality, diverse training data.

**Model Building and Training**    
Our experimentation platform designs and executes optimal model-building experiments tailored to your use case on any cloud provider. We consistently deliver high-performing custom models by integrating state-of-the-art techniques such as SFT, DPO, RLHF, and building compound models.

**Deployment**    
Seamlessly deploy customized AI models using VLLM / Fastchat with a single command. 

## Example Notebooks

Here are some example notebooks demonstrating Leeroo's capabilities:

1. [leeroo_text_to_sql.ipynb](https://colab.research.google.com/drive/1asatSBWUoMggk11byScVOBz_tszopiFw?usp=sharing) - Demonstrates how to use Leeroo for text-to-SQL tasks.
2. [leeroo_math_tutor.ipynb](https://colab.research.google.com/drive/1e3bqdaKOy4ZWVtTAamrEUNgTd11uLcMR?usp=sharing) - Showcases the use of Leeroo in creating a personalized math tutoring model.
3. [leeroo_coding_tutor.ipynb](https://colab.research.google.com/drive/164MYXPAzVWrx1cQNugdKb112G-utIx3Y?usp=sharing) - Provides an example of building a custom coding tutor with Leeroo.
