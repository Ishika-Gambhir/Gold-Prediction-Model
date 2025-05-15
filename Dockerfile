# 1. Use an official Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy everything into the container
COPY . .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port Streamlit uses
EXPOSE 8501

# 6. Run the Streamlit app
CMD ["streamlit", "run", "frontend.py"]
