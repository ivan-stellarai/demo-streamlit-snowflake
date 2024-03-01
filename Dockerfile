FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install streamlit
RUN pip install snowflake-snowpark-python
RUN pip install ipywidgets
# Copy the rest of the application
COPY . /app/
