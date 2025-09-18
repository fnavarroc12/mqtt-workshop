FROM jupyter/scipy-notebook:latest

# Set the working directory in the container
WORKDIR /app

# Expose the Jupyter Lab port
EXPOSE 8888

COPY . .
RUN pip install -r /app/requirements.txt

# Install additional packages if needed
RUN pip install --no-cache-dir \
    matplotlib \
    seaborn \
    plotly \
    jupyter-lab

# Set default command to start Jupyter Lab
CMD ["start.sh", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]