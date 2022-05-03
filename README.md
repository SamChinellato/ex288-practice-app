# ex288-practice

A silly flask app to practice a few commands for EX288.


## Challenges:

### 1. Deploy the application 
* Use the `new-app` command to deploy the application
* Deploy the application in a new project called `flask-app`
* The application should be called `flask-practice` and should be deployed with the `oc new-app` command.
* Expose the app's service to a route

Once deployed the following curl should return a message:

```
curl http://$(oc get route -n ex288-practice flask-practice -ojsonpath='{..host}')



<p>Hello, World! This is my EX288 practice flask app!</p><p>Hello, World! This is my EX288 practice flask app!</p>
```

### 2. Set the application environment

### 3. Health check

### 4.  Set post-commit build hook

### 5. Expose the registry and redeploy the application 

