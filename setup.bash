#!/bin/bash

sudo apt update -y && sudo apt upgrade -y
sudo apt install nginx -y
sudo git config credential.helper store

echo 'server {
  listen 80;
  listen [::]:80;
  
  server_name 18.141.137.176;

  location / {
    proxy_pass http://127.0.0.1:3000;
  } 
  
  location /api {
    proxy_pass http://127.0.0.1:8000;
  } 
}' >> /etc/nginx/conf.d/django.conf

sudo service nginx start