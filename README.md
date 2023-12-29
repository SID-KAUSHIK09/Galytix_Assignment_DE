# Galytix Assignment

Welcome to the Galytix Assignment repository! This project includes modules for initializing a pipeline and processing data for similarity calculation.

## Introduction

This project aims to provide a solution for the Galytix assignment. It includes modules written in Python for setting up the pipeline and processing data to calculate similarity between phrases.

## Project Structure

- **init_pipeline.py**: Module for initializing the pipeline.
- **process_data.py**: Module for processing data and calculating similarity.
- **vectors.bin**: Binary file containing word embeddings.
- **phrases.csv**: CSV file containing phrases data.
- **setup.py**: Script for setting up the project.

## How to run
-First download the pretrained set of Word2Vec vectors from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM
-Then run init_pipeline.py, it'll generate vectors.bin.
-Then run process_data.py, inside it there is main func where you can write any phrase and it'll return closest match from phrases.csv with distance.

## Author
- [Siddharth Kaushik](https://github.com/SID-KAUSHIK09)
