# Collekt - Track your collection

Collekt is a service that tracks new offers on ebay and co. to extend the collection of your favorite things. 

## Docker

You can install our service via Docker. Clone this repository into a folder of your choice.
Then, open a Terminal and execute the command ```docker-compose up -d```.
Wait for everything to finish installing and starting up.
If you have done everything correctly, you can start the web interface by opening ```localhost```.

## Jaeger

Jaeger is a tracing tool that is used to trace the request of our frontend, backend and our logic layer through microservices.
Tracing can be used for:
- Performance analysis: identification of bottlenecks and latencies
- Fault Localization: shows faulty service dependencies
- Dependency analysis: visualizes service communication

To test our Jaeger implementation you can open localhost/jaeger to open the tool. Choose our Collekt service and then the
operation you want to analyze.
