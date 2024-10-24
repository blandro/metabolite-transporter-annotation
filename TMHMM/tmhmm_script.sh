#!/bin/bash
#
#SBATCH --job-name=tmhmm_predictions
#SBATCH --output=tmhmm_output_%j.txt
#SBATCH --error=tmhmm_error_%j.txt
#
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=200M
#SBATCH --time=00-01:00:00
#
/triumvirate/home/benjalan/.conda/envs/msc/bin/python3 tmhmm_program.py