### **Dockerizing Django TODO Application**

#### **Step 1: Install Docker Engine**

1. **Install Docker Engine:**
   - Install Docker Engine on your local machine.

#### **Step 2: Clone Project Files**

2. **Clone Project Files:**
   - Use `git clone` to download all project files from GitHub.

#### **Step 3: Create Dockerfile**

3. **Create Dockerfile:**
   - Create a Dockerfile in the project directory with the following content:

```Dockerfile
# Stage 1: Build
FROM python:3.8 AS build

WORKDIR /app
COPY . /app

# Stage 2: Production
FROM python:3.8-slim

COPY --from=build /app /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### **Step 4: Build Docker Image**

4. **Build Docker Image:**
   - Execute the following command to build the Docker image:
     ```bash
     docker build -t todo-dis .
     ```

#### **Step 5: Run Docker Container**

5. **Run Docker Container:**
   - Start a Docker container using the built image:
     ```bash
     docker run -p 8000:8000 todo-dis
     ```

#### **Step 6: Browse Localhost**

6. **Browse Localhost:**
   - Open a web browser and navigate to `localhost:8000` to test if the Django application is running successfully.

#### **Step 7: Push to GitHub**

7. **Push Dockerfile to GitHub:**
   - Commit and push the Dockerfile to your GitHub repository.

#### **Step 8: Docker Image Tagging**

8. **Docker Image Tagging:**
   - Tag the Docker image before pushing to Docker Hub:
     ```bash
     docker tag todo-dis srihari001/todo-dis
     ```

#### **Step 9: Docker Image Push**

9. **Docker Image Push:**
   - Push the Docker image to Docker Hub:
     ```bash
     docker push srihari001/todo-dis
     ```

### **Conclusion:**

Successfully Dockerized the Django TODO application by creating a Dockerfile, building an image, and testing the container locally. The Docker image was then pushed to GitHub and tagged before being pushed to Docker Hub for further deployment or distribution.