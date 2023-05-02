#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /ect/nginx/conf.d/default.conf
nginx -g 'daemon off;'