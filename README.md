# 🍀 Automated GitOps & CI/CD Project: From Code to Cluster

Hey there! Welcome to my end-to-end DevOps project. Instead of just deploying things manually, I built a completely automated pipeline. When I push new code to GitHub, a continuous integration (CI) pipeline builds it, updates the configuration, and a GitOps engine automatically deploys it onto a live local Kubernetes cluster. 

No manual clicking, no messy manual server commands—just pure automation.


## 🛠️ The Tech Stack (What I Used)

* **Infrastructure as Code (IaC):** Terraform (Using `scott-the-programmer/minikube` to spin up our cluster)
* **The App:** A Python Flask app that generates daily lucky numbers.
* **Containerization:** Docker (To pack the app nicely so it runs anywhere).
* **Package Management:** Helm Charts (To make our Kubernetes files dynamic and easy to update).
* **CI Automation:** GitHub Actions (To build images and update configuration automatically).
* **GitOps Delivery (CD):** ArgoCD (To make sure what's on GitHub is exactly what's running on our cluster).


## 🗺️ How It All Works (The Big Picture)

1. **Write Code & Push:** I make a change to my Python app or configurations and push it to GitHub.
2. **The Build Engine Sparks:** GitHub Actions wakes up, builds a fresh Docker image, tags it with a unique short commit ID, and pushes it to DockerHub.
3. **The Automated Write-Back:** The GitHub pipeline automatically edits my Helm chart (`values.yaml`) to use the brand new image tag.
4. **GitOps Takes Over:** ArgoCD notices that GitHub has changed. It immediately updates my Minikube cluster so the live application matches the new code.


## 🧗‍♂️ Real-World Challenges I Faced & Fixed

DevOps is rarely smooth sailing on the first try! Here are the real-world bugs I encountered and broke through during this build:

* **The Massive File Git Block:** I accidentally tracked a massive 65MB Windows execution binary (`argocd.exe`) into my Git history. GitHub rejected it! I used `git rm` to purge it completely from my tracking tree and updated `.gitignore` with `*.exe` to make sure it never happens again.
* **The Git Push Rejection:** When trying to push fixes, GitHub blocked me because my local git history was behind the remote changes. I used `git stash` to save my work safely on the side, ran `git pull origin main --rebase` to smoothly catch up with the remote branch, and popped my stash back to push cleanly.
* **The Helm `nil pointer` Crash:** My application crashed at first because my Helm template looked for an `httpRoute.enabled` setting that wasn't declared yet. I jumped into `values.yaml` and explicitly defined fallback blocks to fix it.



## 🕹️ Step-by-Step Practice Guide

If you want to spin this up or interact with the cluster, use this handy command cheat sheet:

### 1. Provisioning the Cluster with Terraform
```powershell
# Initialize Terraform and download the Minikube provider
terraform init

# Double check what Terraform is about to build
terraform plan

# Build the local cluster and spin up ArgoCD automatically
terraform apply -auto-approve



2. Overcoming Git Hurdles (The Rebase Rescue)
If you ever get stuck pushing changes because your local repository is out of sync with GitHub, do this:


# 1. Save your uncommitted work safely on a side shelf
git stash

# 2. Pull remote changes and slide your local history smoothly on top
git pull origin main --rebase

# 3. Take your work off the shelf and put it back into your project
git stash pop

# 4. Push safely to GitHub!
git push origin main



3. Log into ArgoCD like a Pro


# Fetch and decode the secret admin password from your cluster
(kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}") | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }

# Log into the ArgoCD CLI tool
argocd login localhost:8081 --username admin --password <YOUR_DECODED_PASSWORD> --insecure

# Link this GitHub repo securely to ArgoCD using a Personal Access Token
argocd repo add https://github.com/Stanleyoluebube/DevOps-Project.git --username Stanleyoluebube --password <YOUR_GITHUB_TOKEN> --server localhost:8081 --insecure

# Apply the GitOps application map
kubectl apply -f argocd-app.yml

# Force ArgoCD to check for new changes immediately
argocd app get devops-project --hard-refresh



4. Testing & Verifying the App


# See everything running in your cluster namespaces
kubectl get pods --all-namespaces

# Check if your app's networking routes are live
kubectl get endpoints -n default

# Tunnel into your cluster and view your live Flask app on http://localhost:8080
kubectl port-forward pod/<YOUR-LIVE-POD-NAME-FROM-LOGS> 8080:8080 -n default
