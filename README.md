# shopscale-aws-autoscaling
Scalable Flask e-commerce application deployed on AWS using EC2, Application Load Balancer, Auto Scaling Group, RDS MySQL, Docker and Locust.

## Overview

This project demonstrates how to deploy a web application on AWS
and automatically scale EC2 instances based on CPU utilization.

The application is deployed using Flask and Gunicorn on Ubuntu EC2
instances. Amazon RDS MySQL is used as the backend database.

An Application Load Balancer distributes incoming traffic across
healthy EC2 instances managed by an Auto Scaling Group.

Locust running inside Docker is used to generate load and demonstrate
automatic scale-out and scale-in behavior.

## Architecture

                    Internet
                       |
                       v
              Application Load
                   Balancer
                       |
                       v
                 Target Group
                       |
             +---------+---------+
             |                   |
             v                   v
          EC2 #1              EC2 #2
             |                   |
             +---------+---------+
                       |
                       v
                  RDS MySQL


        Locust EC2
          Docker
            |
            v
           ALB


## Technologies Used

1. AWS
2. Amazon EC2
3. Application Load Balancer
4. Auto Scaling Group
5. Amazon RDS MySQL
6. Amazon VPC
7. Security Groups
8. Amazon Machine Image (AMI)
9. Launch Template

## Application

1. Python
2. Flask
3. Gunicorn
4. MySQL
5. HTML
6. CSS
7. JavaScript

## DevOps / Testing
1.Docker
2.Locust
3.Linux
4.systemd

## Application

The Flask application provides:

1. Product listing
2. Product search
3. Shopping cart API
4. Health check endpoint
5. Web-based product interface

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | ShopScale home page |
| GET | `/health` | Application and database health check |
| GET | `/api/products` | Get all products |
| GET | `/api/search?q=` | Search products |
| POST | `/api/cart` | Add product to cart |

## Deployment Process

1. Launch Ubuntu EC2 instance.
2. Install Python and required packages.
3. Create Python virtual environment.
4. Deploy Flask application.
5. Configure RDS MySQL.
6. Import database schema and seed data.
7. Configure environment variables.
8. Configure Gunicorn with systemd.
9. Create a custom AMI.
10. Create an Application Load Balancer.
11. Create a Target Group with `/health` checks.
12. Create a Launch Template.
13. Create the Auto Scaling Group.
14. Configure CPU target tracking.
15. Verify ALB → EC2 → RDS connectivity.

## Future Improvements

1. HTTPS using ACM
2. Route 53 custom domain
3. AWS Secrets Manager
4. CloudWatch dashboards and alarms
5. CI/CD using GitHub Actions
6. Infrastructure as Code using Terraform
7. Containerized application deployment
8. Amazon ECS/EKS
9. HTTPS-only ALB configuration
