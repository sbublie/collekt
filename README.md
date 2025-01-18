# Collekt - Track your collection

Collekt is a service that tracks new offers on ebay and co. to extend the collection of your favorite things.
We created this for you to follow along this instructions to get a good overview how Jaeger and Distributed Tracing works.

## What is Jaeger?

Jaeger is a tracing tool that is used to trace the request of our frontend, backend and our logic layer through microservices.
Tracing can be used for:
- Performance analysis: identification of bottlenecks and latencies
- Fault Localization: shows faulty service dependencies
- Dependency analysis: visualizes service communication

If you follow the following three step you'll get a basic understanding what Jaeger does.

## Step 1: Get Docker Containers running

You can install our service via Docker.
Open a Terminal and execute the command 
```
docker-compose up -d
```
Wait for everything to finish installing and starting up.
If you have done everything correctly, you can get to the web interface by navigating to [localhost](http://localhost). If port 80 is blocked on your machine, please adjust the port mapping in the compose file.

## Step 2: Send first trace to Jaeger

Now we want to send our first trace to Jaeger. Therefore you can use the Python script ```tracing_example``` in the ```backend``` folder. But you might want to create a virtual environment and install the required dependencies (reqirements.txt) first.

In this script we manually create a trace and fill it with two spans. We simulate workload with `time.sleep(1)`.

After you executed the script, a trace with the name `my-otel-service` should be visible in the [Jaeger UI](http:localhost/jaeger).

## Step 3: Analyze Collekt traces

In the real world nobody would manually create/build traces. For most frameworks there are pre-built instrumentations. In our app we use an instrumentation for FastAPI (see `backend/app.py`). If you head back to the Collekt UI you can add or delete entries to the wishlist and then see the following request to the backend in Jaeger.   

The architecture diagram of the app can be found on [this site](http://localhost/docs)
