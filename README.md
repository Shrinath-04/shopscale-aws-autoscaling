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

AWS
Amazon EC2
Application Load Balancer
Auto Scaling Group
Amazon RDS MySQL
Amazon VPC
Security Groups
Amazon Machine Image (AMI)
Launch Template

## Application

Python
Flask
Gunicorn
MySQL
HTML
CSS
JavaScript

## DevOps / Testing
Docker
Locust
Linux
systemd

## Application

The Flask application provides:

Product listing
Product search
Shopping cart API
Health check endpoint
Web-based product interface

## API Endpoints

GET  /
GET  /health
GET  /api/products
GET  /api/search?q=<query>
POST /api/cart

## Deployment Process
Launch Ubuntu EC2 instance.
Install Python and required packages.
Create Python virtual environment.
Deploy Flask application.
Configure RDS MySQL.
Import database schema and seed data.
Configure environment variables.
Configure Gunicorn with systemd.
Create a custom AMI.
Create an Application Load Balancer.
Create a Target Group with /health checks.
Create a Launch Template.
Create the Auto Scaling Group.
Configure CPU target tracking.
Verify ALB to EC2 to RDS connectivity.

## Future Improvements

HTTPS using ACM
Route 53 custom domain
AWS Secrets Manager
CloudWatch dashboards and alarms
CI/CD using GitHub Actions
Infrastructure as Code using Terraform
Containerized application deployment
Amazon ECS/EKS
HTTPS-only ALB configuration
