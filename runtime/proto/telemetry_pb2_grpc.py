# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import telemetry_pb2 as telemetry__pb2

GRPC_GENERATED_VERSION = '1.73.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in telemetry_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TelemetryServiceStub(object):
    """The service definition for receiving telemetry from Arc Runtime.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamTelemetry = channel.stream_unary(
                '/arc.telemetry.v1.TelemetryService/StreamTelemetry',
                request_serializer=telemetry__pb2.TelemetryEvent.SerializeToString,
                response_deserializer=telemetry__pb2.StreamTelemetryResponse.FromString,
                _registered_method=True)


class TelemetryServiceServicer(object):
    """The service definition for receiving telemetry from Arc Runtime.
    """

    def StreamTelemetry(self, request_iterator, context):
        """A client-streaming RPC.
        The runtime client opens a stream and sends a sequence of events.
        The server processes them as a batch once the client closes the stream.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TelemetryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamTelemetry': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamTelemetry,
                    request_deserializer=telemetry__pb2.TelemetryEvent.FromString,
                    response_serializer=telemetry__pb2.StreamTelemetryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arc.telemetry.v1.TelemetryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arc.telemetry.v1.TelemetryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TelemetryService(object):
    """The service definition for receiving telemetry from Arc Runtime.
    """

    @staticmethod
    def StreamTelemetry(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/arc.telemetry.v1.TelemetryService/StreamTelemetry',
            telemetry__pb2.TelemetryEvent.SerializeToString,
            telemetry__pb2.StreamTelemetryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
