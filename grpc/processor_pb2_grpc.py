# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import processor_pb2 as processor__pb2

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
        + f' but the generated code in processor_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DataProcessorStub(object):
    """Servicio que define dos métodos: uno unario y otro streaming.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessData = channel.unary_unary(
                '/processor.DataProcessor/ProcessData',
                request_serializer=processor__pb2.DataRequest.SerializeToString,
                response_deserializer=processor__pb2.DataResponse.FromString,
                _registered_method=True)
        self.StreamData = channel.unary_stream(
                '/processor.DataProcessor/StreamData',
                request_serializer=processor__pb2.DataRequest.SerializeToString,
                response_deserializer=processor__pb2.DataResponse.FromString,
                _registered_method=True)


class DataProcessorServicer(object):
    """Servicio que define dos métodos: uno unario y otro streaming.
    """

    def ProcessData(self, request, context):
        """Método unario: procesa la lista de números devolviendo la suma.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamData(self, request, context):
        """Método de server streaming: envía progresivamente la suma acumulada.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataProcessorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessData': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessData,
                    request_deserializer=processor__pb2.DataRequest.FromString,
                    response_serializer=processor__pb2.DataResponse.SerializeToString,
            ),
            'StreamData': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamData,
                    request_deserializer=processor__pb2.DataRequest.FromString,
                    response_serializer=processor__pb2.DataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'processor.DataProcessor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('processor.DataProcessor', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DataProcessor(object):
    """Servicio que define dos métodos: uno unario y otro streaming.
    """

    @staticmethod
    def ProcessData(request,
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
            '/processor.DataProcessor/ProcessData',
            processor__pb2.DataRequest.SerializeToString,
            processor__pb2.DataResponse.FromString,
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
    def StreamData(request,
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
            '/processor.DataProcessor/StreamData',
            processor__pb2.DataRequest.SerializeToString,
            processor__pb2.DataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
