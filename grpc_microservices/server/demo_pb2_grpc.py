# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import demo_pb2 as demo__pb2

GRPC_GENERATED_VERSION = '1.71.0'
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
        + f' but the generated code in demo_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DemoServiceStub(object):
    """Definición del servicio gRPC
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/demo.DemoService/SendMessage',
                request_serializer=demo__pb2.MessageRequest.SerializeToString,
                response_deserializer=demo__pb2.MessageResponse.FromString,
                _registered_method=True)
        self.StreamMessages = channel.unary_stream(
                '/demo.DemoService/StreamMessages',
                request_serializer=demo__pb2.MessageRequest.SerializeToString,
                response_deserializer=demo__pb2.MessageResponse.FromString,
                _registered_method=True)


class DemoServiceServicer(object):
    """Definición del servicio gRPC
    """

    def SendMessage(self, request, context):
        """Método unario: recibe un mensaje y retorna una respuesta.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMessages(self, request, context):
        """Método con respuesta en streaming: recibe un mensaje y retorna un stream de respuestas.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DemoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=demo__pb2.MessageRequest.FromString,
                    response_serializer=demo__pb2.MessageResponse.SerializeToString,
            ),
            'StreamMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMessages,
                    request_deserializer=demo__pb2.MessageRequest.FromString,
                    response_serializer=demo__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'demo.DemoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('demo.DemoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DemoService(object):
    """Definición del servicio gRPC
    """

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/demo.DemoService/SendMessage',
            demo__pb2.MessageRequest.SerializeToString,
            demo__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StreamMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/demo.DemoService/StreamMessages',
            demo__pb2.MessageRequest.SerializeToString,
            demo__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
