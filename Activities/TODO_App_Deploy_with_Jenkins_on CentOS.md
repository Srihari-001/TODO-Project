## DEPLOYING DJANGO TODO APPLICATION ON CENTOS VM WITH ORACLE VM VIRTUALBOX

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
- Jenkins
- Jenkins Publish Over SSH Plugin

### **Pre-requisite:**
- Django project with source code hosted on GitHub.
- Oracle VM VirtualBox and Vagrant installed.
- GitBash installed.
- Jenkins set up on personal machine.
- Basic familiarity with CentOS, Django, and virtual environments.

### **Steps:**

#### **Setting up the CentOS VM:**
1. Use GitBash to interface with the system.
2. Initialize a CentOS environment in Oracle VM VirtualBox via Vagrant commands:
   ```bash
   vagrant init centos/7
   vagrant up
   ```

#### **Access the VM: Using GitBash:**
1. 
   ```bash
   vagrant ssh
   ```

#### **Environment Setup:**
1. Update CentOS package repository and install essentials:
   ```bash
   sudo yum update
   sudo yum install -y python3 python3-pip git
   ```
2. Clone the Django TODO project using Git:
   ```bash
   git clone https://github.com/Srihari-001/TODO-Project.git
   cd TODO-Project/
   ```

#### **Copy VM IP:**
1. Retrieve the VM IP address, for instance, using:
   ```bash
   ip addr show
   ```

#### **Open Jenkins in Personal Machine Browser:**

1. Navigate to Jenkins dashboard.

#### **Jenkins Setup:**
1. Go to **Manage Jenkins > Manage Plugins**.
2. Install **Publish Over SSH** plugin.
3. Navigate to **Manage Jenkins > Configure System**.
4. In the SSH Server section, add the details:
   - **Name:** `centos`
   - **Hostname:** [VM IP]
   - **Username:** `srihari`
   - **Remote Directory:** `/`

### **Setting Up SSH Keys:**

#### **Generating SSH Key Pair:**

On your Jenkins machine (or any Linux/Unix based system):

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

This will generate two files, `id_rsa` (private key) and `id_rsa.pub` (public key) in the `~/.ssh/` directory.

#### **Adding the Public Key to CentOS VM:**

Copy the content of `id_rsa.pub` and add it to the `~/.ssh/authorized_keys` file on your CentOS VM:

```bash
echo 'content_of_id_rsa.pub' >> ~/.ssh/authorized_keys
```

#### **Configuring Jenkins with the Private Key:**

In Jenkins, under the "Publish Over SSH" plugin settings:

1. In **Advanced**, click on "Add" next to SSH Key.
2. Use the "Enter directly" option and paste the entire content of the `id_rsa` (private key) file.
3. Save the configuration.

This establishes a secure, password-less connection between Jenkins and the CentOS VM.

#### **Jenkins Job Configuration:**

1. On the Jenkins dashboard, click on **New Item**.
2. Enter the name as "TODO Project" and select "Freestyle Project".
3. Under **Source Code Management**, select **Git**:
   - Repository URL: `https://github.com/Srihari-001/TODO-Project.git`

### **Setting Up Personal Access Token on GitHub:**

1. Login to GitHub and go to **Settings** (click your profile picture at the top right -> Settings).
2. On the left sidebar, select **Developer settings**.
3. Choose **Personal access tokens** and then click **Generate new token**.
4. Give your token a name, set the desired permissions (for repo access, select the `repo` scope).
5. Click **Generate token** at the bottom.
6. **Important:** Copy the generated token immediately as you won't be able to see it again. Store it securely.

#### **Using the Token in Jenkins:**

In Jenkins job configuration, under **Source Code Management**:

1. For **Credentials**, click "Add" -> "Jenkins".
2. Choose "Secret text" and paste the GitHub Personal Access Token.
3. Use the added

 credentials for pulling the repository.

#### **Ensuring GitHub Webhook Operation:**

When you set "GitHub hook trigger for GITScm polling" in Jenkins, it expects a webhook to be set on the GitHub repository to notify Jenkins of code changes.

1. On your GitHub repository, go to **Settings** -> **Webhooks**.
2. Click **Add webhook**.
3. For **Payload URL**, provide `http://YOUR_JENKINS_URL/github-webhook/`.
4. Ensure the Content type is `application/json`.
5. Select the events you want (typically "Just the push event").
6. Add the webhook.

Now, any push to the repository should trigger the Jenkins job.

#### **Trigger Jenkins Job:**

1. Commit changes to the GitHub repo.
2. Verify build status in Jenkins through **Console Output**.
3. Access the application using the VM IP: `http://[VM IP]:8000/`.

#### **Post Validation Tasks:**
1. SSH into the VM.
2. Check for `runserver` processes:
   ```bash
   ps aux | grep "runserver"
   ```
3. Identify any process ID associated with `runserver`.
4. Terminate the process (if necessary):
   ```bash
   kill -9 [process ID]
   ```

### **Lessons Learnt:**
- **User Management:** Always operate under a non-root user for application-related tasks. It ensures system security and avoids accidental system-wide changes.
- **Virtual Environment:** Use virtual environments to avoid package conflicts and maintain project dependencies efficiently.
- **Requirements:** Always maintain a `requirements.txt` to keep track of the project dependencies. This aids in setting up the environment seamlessly on different systems.
- **Jenkins Automation:** Jenkins provides seamless integration and automation for deploying applications.

### **Conclusion:**