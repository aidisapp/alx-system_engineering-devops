# Understanding Web Infrastructure Design

### Basics of Networking:

Understanding the fundamental concepts of networking, including IP addressing, subnetting, routing, and protocols like TCP/IP and UDP, is essential. Additionally, familiarity with network hardware such as routers, switches, and firewalls is crucial for building robust network architectures.

### Server Overview:

A server serves as a central system that provides resources, data, or services to other computers, known as clients, across a network. Servers can fulfill various roles, including file storage, web hosting, email services, database management, and more.

### Introduction to Web Servers:

Web servers are specialized servers responsible for delivering web content to clients over the internet or an intranet. They handle requests from web browsers and respond with the requested web pages, typically using HTTP or HTTPS protocols. Examples of web servers include Apache HTTP Server, Nginx, Microsoft Internet Information Services (IIS), etc.

### Understanding DNS (Domain Name System):

DNS is a decentralized naming system used to translate domain names (e.g., www.example.com) into IP addresses that computers use to identify each other. It plays a vital role in mapping human-readable domain names to numerical IP addresses, enabling seamless internet communication.

### Load Balancing Techniques:

Load balancers distribute incoming network traffic across multiple servers to ensure high availability and reliability. By evenly distributing traffic, load balancers prevent individual servers from becoming overwhelmed, thereby improving performance and scalability. Load balancers can operate at various layers of the OSI model and can be hardware-based or software-based.

### Monitoring System Performance:

Monitoring involves the continuous observation and analysis of system or network performance metrics. Monitoring tools collect data on metrics such as CPU usage, memory utilization, network traffic, and application performance. This data helps identify issues, troubleshoot problems, and optimize system performance.

### Overview of Databases:

Databases store structured data electronically, allowing users to efficiently store, retrieve, manipulate, and manage data. Examples include relational databases like MySQL, PostgreSQL, NoSQL databases like MongoDB, and cloud-based solutions like Amazon RDS, Google Cloud SQL, etc.

### Differentiating Web Servers and App Servers:

While web servers primarily serve static content over the web, app servers host and execute application logic, handling dynamic content generation and processing client requests.

### Common DNS Record Types:

DNS records serve various purposes, including mapping domain names to IP addresses (A records), handling mail exchange (MX records), and specifying authoritative name servers for domains (NS records).

### Understanding Single Points of Failure:

Single points of failure are components within a system whose failure can lead to system-wide downtime. Identifying and mitigating single points of failure is critical for ensuring system reliability and uptime.

### Strategies for Deploying New Code:

Rolling deployments, blue-green deployments, and canary deployments are strategies used to deploy new code with minimal downtime and risk of disruption to the system.

### High Availability Clusters:

High availability clusters are interconnected systems designed to ensure continuous operation and minimize downtime. They can be configured as active-active or active-passive setups to provide redundancy and fault tolerance.

### Secure Communication with HTTPS:

HTTPS is a secure version of HTTP that encrypts data transmitted between web servers and clients, ensuring confidentiality, integrity, and authentication of data exchanged over the internet.

### Importance of Firewalls:

Firewalls are essential network security devices or software that monitor and control incoming and outgoing network traffic based on predefined security rules. They serve as a barrier between trusted internal networks and untrusted external networks, protecting against unauthorized access and cyber threats. Firewalls can be implemented as hardware appliances, software applications, or a combination of both.