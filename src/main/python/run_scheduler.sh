#!/bin/bash

# Activate virtual environment if you're using one
# source venv/bin/activate

# Change to the script directory
cd "$(dirname "$0")"

# Run the scheduler
python3 scheduler.py 