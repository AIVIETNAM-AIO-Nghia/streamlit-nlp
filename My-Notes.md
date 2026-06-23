# Day 1

## Streamlit

A framework used Python to replace HTML, CSS for web interface. It is designed for rapid data-app prototyping, not robust, enterprise-scale web development.
To install Streamlit, we use PIP (Python package manager):
**_"pip install streamlit"_**

## To run the streamlit app on Google Colab
Need to install localtunnel to expose the port of the runtime to public internet.
Install localtunnel:
**_"npm install localtunnel"_**
Running the source code file:
**_"streamlit run main.py &>/content/logs.txt & npx localtunnel --port 8501"_**
Log is save to logs.txt file
