# Leeroo Client

<img alt="Leeroo logo" src="https://github.com/Leeroo-AI/mergoo/blob/main/static/logo.png?raw=true" width="148" align="right" />

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-green.svg)](#python)
[![Version](https://img.shields.io/pypi/v/mergoo?color=blue)](https://pypi.org/project/leeroo-client/)


**Leeroo Dager** offers a comprehensive solution for developing custom AI models. By simply defining your evaluation system, and providing seed data, Leeroo automates the entire workflow from data generation to model training and evaluation. No AI expertise is required—Leeroo ensures the delivery of the best customized model tailored to your specifications. Model deployment is streamlined and can be achieved with a single command.

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

**Synthetic Data Generation**    
Our advanced data generation pipeline employs multi-agent systems to create diverse training data, ensuring enhanced generalization and reliability.

**Training**    
Our training pipeline is designed to execute optimal experiments tailored to your use case on any cloud provider. By integrating state-of-the-art techniques such as SFT, DPO, RLHF or building compound models, we consistently deliver high-performing custom models.

**Evaluation**    
Utilize our Multi-Model LLM System to create high-quality LLM as judge Evaluation systems. 

**Deployment**    
Automatically deploy customized AI models without the need for AI Infra expertise. Uses VLLM / Fastchat for deployment. 
