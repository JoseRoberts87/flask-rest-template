# Setup

## Getting Started

This repo assusmes that developers have some common knowledge about the tools and resources used and does not cover or attempts to be a comprehensive guide on how to run the code without any software development knowledge

### Main Dependencies

- python 3.10.1
- Poertry
- Terraform
- git-crypt

## Setup Local Dev Environment

having the above main dependencies installed, create a virtual environment and activate it. Once the virtual environment has been activated, run `poetry install` in the terminal to install and manage all of the repo dependencies.

## Local Dev Environment Variables

the code makes use of environment variables (envvars) to configure and create context for the code that runs. using the envvars, we can change the salesforce and db connections without having to change or touch the code. Create a file named `.env ` at the root of the directory
