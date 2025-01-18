import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

# Define the service name
resource = Resource.create({"service.name": "my-otel-service"})

# Step 1: Set up the Tracer Provider
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Step 2: Configure OTLP Exporter (sends traces to Jaeger)
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

# Step 3: Add the OTLP exporter to the TracerProvider
span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)

# Get a tracer
tracer = trace.get_tracer("my-otel-service")

# Step 4: Create and send a trace
with tracer.start_as_current_span("parent-span") as parent:
    parent.set_attribute("custom-tag", "parent-span")
    time.sleep(0.5)

    with tracer.start_as_current_span("child-span") as child:
        child.set_attribute("custom-tag", "child-span")
        time.sleep(1)

print("Traces sent to Jaeger!")
