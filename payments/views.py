from rest_framework import permissions
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from payments import serializers, models



class PaymentView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def payment_success_webhook(request):
    print(f'success {request.data}')
    return Response(request.data)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def payment_check_webhook(request):
    print(f'check {request.data}')
    return Response(request.data)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def payment_result_webhook(request):
    data = request.data
    instance = models.Payments.objects.get(order_id=data['order'])
    if instance.status == models.Payments.Status.PENDING:
        status = data['status']['code']
        if status == 'success':
            instance.status = models.Payments.Status.SUCCESS
        else:
            instance.status = models.Payments.Status.FAIL
        instance.save()
    return Response(request.data)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def payment_failure_webhook(request):
    print(f'failure {request.data}')
    return Response(request.data)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def back_callback(request):
    print(f'back {request.data}')
    return Response(request.data)


@api_view()
@permission_classes([permissions.IsAuthenticated])
def get_payment(request, order_id):
    return Response(order_id)



@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def post_callback(request):
    import pdb
    pdb.set_trace()