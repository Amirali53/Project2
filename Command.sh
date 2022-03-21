#!/usr/bin/env bash
# this script contain all Azure CLI commands you used

# Create an App Service in Azure.
az webapp up -n amir-flaskpipelines -g amir-udacity-rg

# view the logs:
az webapp log tail -n amir-flaskpipelines -g amir-udacity-rg
