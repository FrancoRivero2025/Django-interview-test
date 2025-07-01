FROM nginx:1.28.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN rm -rf /usr/share/nginx/html/*
