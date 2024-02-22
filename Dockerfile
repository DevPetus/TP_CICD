#Setting base image to python 3.12.1
FROM python:3.12.1 

# Copy math.py into container
COPY math.py .

# Run math.py tests
CMD python -m unittest math.py