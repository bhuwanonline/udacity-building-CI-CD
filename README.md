[![Python application test with Github Actions](https://github.com/bhuwanonline/udacity-building-CI-CD/actions/workflows/main.yml/badge.svg)](https://github.com/bhuwanonline/udacity-building-CI-CD/actions/workflows/main.yml)

Building a CI/CD Pipeline

Overview

In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan

Architectural Diagram (Shows how key parts of the system work)

![image](https://user-images.githubusercontent.com/20974800/211331285-8e183eca-862c-480d-adf3-28e89cc44766.png)


Continuous Integration

CI: Set Up Azure Cloud Shell

1. Create the Cloud-Based Development Environment

  Create a Github repo

  Launch an Azure Cloud Shell environment and create ssh-keys. Upload these keys to your GitHub account.

  Project cloned into Azure Cloud Shell (git clone git@github.com:bhuwanonline/udacity-building-CI-CD.git)

  ![git clone latest files](https://user-images.githubusercontent.com/20974800/211333250-027b3d12-6d97-424a-8c64-bd6372bc4966.png)

  Passing tests that are displayed after running the `make all` command from the `Makefile`
  
  ![make install](https://user-images.githubusercontent.com/20974800/211336205-5136ed4f-514f-4fb3-b820-660bbca8622a.png)

  ![make install complete](https://user-images.githubusercontent.com/20974800/211336260-7eab82aa-252c-4885-ac1b-86d28f324aed.png)


2. Configure GitHub Actions

    Go to your Github Account and enable Github Actions. 
    
    ![github action flow](https://user-images.githubusercontent.com/20974800/211336977-782a80b4-393a-437c-a61e-e83a8717bc26.png)
    
    configure main.yml file
    
    ![Github action using main yaml file](https://user-images.githubusercontent.com/20974800/211337133-6cf0b2e8-278c-4d74-9ef1-04e42462cbec.png)

    Verify remote tests pass in GitHub Actions UI
    
    ![github action build flow steps](https://user-images.githubusercontent.com/20974800/211338000-f2a21254-2d7a-4ca6-a32a-a4063cbed5f8.png)
    
    In order to validate the application before deploy to app service, start the application in the virtual environment:

    python app.py
    
    ![windows local setup python](https://user-images.githubusercontent.com/20974800/211339171-518f09bb-5871-4a2b-83a7-b8bd2d43a10e.png)
  
Deploy the app to an Azure App Service
  
    Create an App Service in Azure. In this example the App Service is called udacity-flask-ml-service

    az webapp up --name udacity-flask-ml-service
    
    ![deploying web app](https://user-images.githubusercontent.com/20974800/211340887-845ec55b-79e4-4309-bfac-d0612b4b1ab1.png)
    
    
    ![azure app services](https://user-images.githubusercontent.com/20974800/211341413-2c9f4d9f-17c5-4263-93c9-86d646e010c8.png)
    
        
    ![Initial changes of home page](https://user-images.githubusercontent.com/20974800/211341491-2509b1c7-39af-4fa4-9c8b-180b9d849ce0.png)

Continuous Delivery

    Prerequisites
    
      Logged into the https://portal.azure.com/

      Logged into the https://dev.azure.com/ in a separate browser tab.

    Create an Azure DevOps project

    Next, we'll need to create an Azure DevOps project and connect to Azure. The screenshots below show the steps, but if you need to, you can also refer to  
    the official documentation for more detail.
        
    1. Create new project and name it
    
    ![image](https://user-images.githubusercontent.com/20974800/211342890-90e626d8-2212-41d4-bc37-486e8d1b6b15.png)


    2. Ensure you set up a new service connection via Azure Resource Manager and Pipeline
    
    
    3. Select Pipeline and create a new one.
    
    ![image](https://user-images.githubusercontent.com/20974800/211342969-d65ec895-4169-4dd6-a356-f46ff899937c.png)
    
    4. Create the GitHub Integration
    
    ![image](https://user-images.githubusercontent.com/20974800/211343318-1102681f-8be7-48ad-bcdb-eee420fff6b8.png)
    
    5. Configure Python to Linux Web App on Azure
    
    ![image](https://user-images.githubusercontent.com/20974800/211343424-75df77a3-a946-432f-bb30-948b8baebd50.png)
    
    6: Set Up the Continuous Delivery Workflow
    
    ![review your pipeline yaml](https://user-images.githubusercontent.com/20974800/211344072-0040458e-9067-4edb-8fd8-1a9530f43d1b.png)




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

<TODO: Add link Screencast on YouTube>


