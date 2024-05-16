# Google Cloud App Engine

Google Cloud App Engine is suitable for a microservice architecture where you
only need to worry about the application code rather than the underlying
infrastructure (or how to scale that infrastructure).
Not every service is suitable for App Engine. We need to make sure we know about
the specific caveats of App Engine before we use it for the deployment platform
of our choice.

## App Engine Standard

For Python development, the App Engine Standard service deploys the application
code in a sandbox environment (most likely automatically creates a Docker
image). We control the configuration of the sandbox using configuration files.
[Getting started Python runtime reference](https://cloud.google.com/appengine/docs/standard/python3/runtime).

The directory structure that Google recommends for storing the code in your
repo can be found [here](https://cloud.google.com/appengine/docs/standard/configuration-files).

When deploying microservices, we need to make sure they can communicate with
each other. App Engine Standard allows this communication simply by calling the
services HTTP endpoint. We can restrict network communication between services
by controlling the "Ingress" settings for the service. By default, any resource
on the internet can access the service via its domain name. We can control this
by specifying the "Ingress" settings. For more info refer these links: https://cloud.google.com/appengine/docs/standard/communicating-between-services, https://cloud.google.com/appengine/docs/standard/ingress-settings.<br>
**Few doubts here, what is the difference between a VPC, Shared VPC, Serverless VPC 
access connector.**


