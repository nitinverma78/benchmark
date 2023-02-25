#!/bin/bash
conda create -y -n dev python=3.10.8
conda install -y -n dev --file=requirements.txt
