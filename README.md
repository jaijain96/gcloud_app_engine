# Google Cloud App Engine

Google Cloud App Engine is suitable for a microservice architecture where you
only need to worry about the application code rather than the underlying
infrastructure (or how to scale that infrastructure).
Not every service is suitable for App Engine. We need to make sure we know about
the specific caveats of App Engine before we use it for the deployment platform
of our choice.

## App Engine Standard

### Getting Started

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
**Doubt here: What is the difference between a VPC, Shared VPC, Serverless VPC 
Access connector, VPC Peering?**

App Engine Standard only supports HTTP/1.1, so any newer protocols such as
HTTP/2 or HTTP/3 are translated to HTTP/1.1 before getting passed to the
application.

When serving static content using App Engine, such as HTML, CSS, JS, image
files, etc, we need to take care that the changes we make are immediately
available to new users. There are caveats for invalidating caches when doing
this which can be found at these links: https://cloud.google.com/appengine/docs/standard/hosting-a-static-website, https://cloud.google.com/appengine/docs/standard/how-requests-are-handled?tab=python. Static content served from App Engine can be hosted via Google
Cloud Storage, Cloud CDN or from within App Engine itself, refer this [doc](https://cloud.google.com/appengine/docs/standard/serving-static-files?tab=python) for more info.

App Engine Standard supports [various routing methods](https://cloud.google.com/appengine/docs/standard/how-requests-are-routed?tab=python). Targeted routing to service
endpoints work as expected but there are some caveats mentioned in the
documentation. For static files or otherwise, there is an option to specify the
"dispatch.yaml" file for routing specific urls and regex url patterns. Google
Cloud Load Balancer based routing is also supported for App Engine services.
**Doubt here: How does Cloud Load Balancer work with App Engine services
on scale?**

App Engine Standard's build process works this way every time a new version is
deployed:
1. App Engine creates a container image using the [Cloud Build](https://cloud.google.com/build/docs) service.
2. Cloud Build builds the container image in the app's region, and runs in the 
App Engine Standard environment.
3. App Engine stores built container images in [Artifact Registry](https://cloud.google.com/artifact-registry/docs). We can download these images to keep or run elsewhere.

App Engine also allows us to deploy an application without routing production
traffic to it. This can then be used to test new versions of a service. Once
satisfied, we can migrate production traffic to it. Refer test and deploy
[docs](https://cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app?tab=python).

The GCloud CLI includes a [local development server](https://cloud.google.com/appengine/docs/standard/tools/using-local-server?tab=python) named "dev_appserver" that
we can run locally to simulate your application running in production App
Engine. This provides an environment which is _closer_ to the production App
Engine environment.

### Configure Your App

App Engine allows to [map a custom domain](https://cloud.google.com/appengine/docs/standard/mapping-custom-domains) to a App Engine service.

For connecting to App Engine service via VPCs, here is the [doc](https://cloud.google.com/appengine/docs/standard/connecting-vpc).

We can use [App Engine security features](https://cloud.google.com/appengine/docs/standard/application-security) in the following ways:
1. App Engine uses HTTPS by default.
2. If we map a custom domain to our App Engine service, App Engine allows using SSL/TSL.
3. We can set up Access Control in GCloud IAM for each App Engine service.
4. App Engine Firewall helps in restricting traffic to/from specific IP
addresses.
5. App Engine also lets us specify Ingress and Egress controls.
6. App Engine also provides various ways to [authenticate users](https://cloud.google.com/appengine/docs/standard/authenticating-users?tab=python).

**Doubt here: How do Ingress and Egress controls differ from Firewall rules?**

### Operate And Maintain

Application Instances are the basic building blocks of App Engine and provide
all resources needed to successfully host our application. App Engine provides
various "Scaling Types" to [manage the scaling of these instances](https://cloud.google.com/appengine/docs/standard/how-instances-are-managed).

App Engine provides ways to [manage](https://cloud.google.com/appengine/docs/standard/migrating-traffic?tab=python) or [split traffic](https://cloud.google.com/appengine/docs/standard/splitting-traffic) between multiple versions of the
same service which can greatly help in testing. There are caveats to do these
so please refer the documents linked above for more info.

App Engine also allows for [scheduling jobs using configuration files](https://cloud.google.com/appengine/docs/standard/scheduling-jobs-with-cron-yaml). A 
cron job makes a scheduled HTTP GET request to the specified endpoint in the
same app where the cron job is configured. The handler for that endpoint
executes the logic when it is called.

App Engine allows to emit logs to Google Cloud Logging from within the
Application code. Structured logging is also supported. Please refer the
[doc](https://cloud.google.com/appengine/docs/standard/writing-application-logs?tab=python) for more info.

Monitoring, alerting and latency information is also available. Please refer
the [doc](https://cloud.google.com/appengine/docs/standard/monitoring-and-alerting-latency). Google Cloud Trace can also be used to
investigate how requests are being routed through your application.



