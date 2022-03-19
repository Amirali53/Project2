# Overview

In this project, you will build a Github repository .....

## Project Plan
It is critical to have an effective project plan and task tracking, In this section you find:

* A [Trello](https://trello.com/b/rJP5K6yR/udacityprojekt2) board for the project
* A [spreadsheet](https://github.com/Amirali53/Project2/blob/62553a880ea0e07507fc0ba2a5d7652843b20104/Project2_Planning.xlsx) that includes the original and final project plan


## Instructions

![_.PNG](Screenshots/_.PNG)

## Deploy the app in Azure Cloud Shell

Go to the azure portal in your browser:
```
git clone git@github.com:Amirali53/Amirali53.git
cd Project2
make setup
source ~/.Project2/bin/activate
make all
python app.py
```


in new browser:
```
./make_prediction.sh
```

```
az webapp up -l westeurope  -n amir-flaskpipelines -g amir-udacity-rg
./make_predict_azure_app.sh
az webapp log tail -n amir-flaskpipelines -g amir-udacity-rg
```


![_](Screenshots/_.PNG) 

In the Azure Portal, select Azure Cloud Shell:

![_](Screenshots/_.PNG) 

In Azure Cloud Shell, clone the repo:
```
git clone git@github.com:_____.git
```
<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

This is the [youtube](https://youtu.be/h3OlWwEk_Tw) link to see a demo


