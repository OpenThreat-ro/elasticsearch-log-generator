### Descriere pentru Docker Hub și GitHub

---

# **Python Log Generator for Elasticsearch (by OpenThreat)**
A lightweight Python-based log generator designed to simulate real-world application logs and send them to **Elasticsearch**. Ideal for testing log pipelines, Kubernetes monitoring setups, and security analysis.

## **Features**
✅ Generates realistic JSON logs similar to a Python microservice  
✅ Simulates multiple services (`auth-service`, `payment-service`, etc.)  
✅ Sends logs directly to Elasticsearch  
✅ Supports **random log levels** (`INFO`, `ERROR`, `DEBUG`, etc.)  
✅ Includes **user IDs, trace IDs, and hostnames** for observability  
✅ Runs efficiently in Kubernetes  

## **Use Cases**
🔹 **Kubernetes logging testing** – Simulate application logs in EFK/ELK stacks  
🔹 **Security monitoring validation** – Generate structured logs for SIEM tools  
🔹 **Incident response training** – Use fake logs to test forensic analysis  
🔹 **Performance testing** – Benchmark log ingestion at scale  

---

### **🚀 Quick Start**

1️⃣ **Pull the image from Docker Hub**  
```sh
docker pull razvan1/elasticsearch-log-generator:latest
```

2️⃣ **Run the container (with default Elasticsearch target)**  
```sh
docker run -e ELASTICSEARCH_HOST="http://my-es-server:9200" -e ELASTICSEARCH_INDEX="custom-logs" razvan1/elasticsearch-log-generator:latest
```

3️⃣ **Deploy in Kubernetes**  
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: log-generator
spec:
  replicas: 2
  selector:
    matchLabels:
      app: log-generator
  template:
    metadata:
      labels:
        app: log-generator
    spec:
      containers:
      - name: log-generator
        image: razvan1/elasticsearch-log-generator:latest
        env:
        - name: ELASTICSEARCH_HOST
          value: "http://elasticsearch.default.svc.cluster.local:9200"
        - name: ELASTICSEARCH_INDEX
          value: "k8s-logs"
```
```sh
kubectl apply -f deployment.yaml
```

---

### **Built with ❤ ️ by OpenThreat**
At **OpenThreat**, we specialize in **security analytics, threat intelligence, and log monitoring solutions**. This tool is part of our ongoing research into **log management, threat detection, and SIEM optimization**. If you're looking for **advanced security monitoring**, get in touch. 🚀  

🔗 **More info: ** [openthreat.ro](#)  
📧 **Contact us: ** contact@openthreat.ro
