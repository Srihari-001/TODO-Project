DEPLOYING DJANGO TODO APPLICATION ON CENTOS VM WITH ORACLE VM VIRTUALBOX

### **Title:**
Deploying Django TODO Application on a CentOS Virtual Machine

### **Aim:**
Deploy a Django application on a CentOS virtual environment and access it externally from any device on the same network.

### **Why:**
Demonstrate understanding and capability in deploying Django applications in virtualized environments. This serves as a hands-on experience in preparation for DevOps roles and real-world deployment scenarios.

### **Tools:**
- Oracle VM VirtualBox
- Vagrant
- GitBash
- CentOS
- Django
- GitHub
- Python3 & pip3
- nohup

### **Pre-requisite:**
- Django project with source code hosted on GitHub.
- Oracle VM VirtualBox and Vagrant installed.
- GitBash installed.
- Basic familiarity with CentOS, Django, and virtual environments.



### **How:**

1. **Setting up the CentOS VM**:
   - Use GitBash to interface with the system.
   - Initialize a CentOS environment in Oracle VM VirtualBox via Vagrant commands:
     ```bash
     vagrant init centos/7
     vagrant up
     ```

2. **Access the VM**:
   Using GitBash:
   ```bash
   vagrant ssh
   ```

3. **Environment Setup**:
   - Update CentOS package repository and install essentials:
     ```bash
     sudo yum update
     sudo yum install -y python3 python3-pip git
     ```

   - Clone the Django TODO project using Git:
     ```bash
     git clone https://github.com/Srihari-001/TODO-Project.git
     cd TODO-Project/
     ```

   - Generate a `requirements.txt` for the project (if not already present). On your development machine with the project running successfully, use:
     ```bash
     pip freeze > requirements.txt
     ```

   - Push `requirements.txt` to the GitHub repository, and pull it in the CentOS VM.

   - Install `virtualenv`:
     ```bash
     pip3 install virtualenv
     ```

   - Create and activate a Python virtual environment within the project directory:
     ```bash
     virtualenv venv
     source venv/bin/activate
     ```

   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **User Management**:
   - For security reasons, it's recommended to avoid using the root user for development. Create a new user named "srihari":
     ```bash
     adduser srihari
     passwd srihari
     ```

   - Switch to this new user:
     ```bash
     su - srihari
     ```

   - Grant necessary permissions to the new user for the project directory:
     ```bash
     chown -R srihari:srihari /path/to/TODO-Project/
     ```

5. **Server Deployment**:
   - Modify `ALLOWED_HOSTS` in `todoproject/settings.py`:
     ```python
     ALLOWED_HOSTS = ['*']
     ```

   - Run Django's development server in the background, making it accessible from all IP addresses:
     ```bash
     nohup python manage.py runserver 0.0.0.0:8000 &
     ```

   - Access the application at:
     ```
     http://192.168.74.10:8000/
     ```

6. **Troubleshooting & Common Issues**:

   1. "Permission denied" error when trying to access `/root` directory. 
      - **Resolution**: Change user permissions using `chown` or switch to a different user.

   2. The Django server stops responding or needs restarting. 
      - **Resolution**: Identify the server process using `ps aux | grep "manage.py runserver"` and terminate it with `kill -9 <PID>`.

7. **Post Deployment**:
   - Check the `nohup.out` file for logs or error messages:
     ```bash
     cat nohup.out
     ```

   - Recommended to delete `nohup.out` post verification:
     ```bash
     rm nohup.out
     ```

### **Lessons Learnt**:

- **User Management**: Always operate under a non-root user for application-related tasks. It ensures system security and avoids accidental system-wide changes.
  
- **Virtual Environment**: Use virtual environments to avoid package conflicts and maintain project dependencies efficiently.

- **Requirements**: Always maintain a `requirements.txt` to keep track of the project dependencies. This aids in setting up the environment seamlessly on different systems.

### **Conclusion**:
Successfully set up a Django application on a CentOS VM. This hands-on process gives a comprehensive insight into the nuances of deployment, preparing the developer for real-world scenarios.

---