from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class AuthMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        # if request.method=='POST':
    #         #     print(request.GET.get('id'))
    #         #     print('333')
    #         #
    #         #     id = request.GET.get('id')
    #         #     if not id:
    #         #         return HttpResponse('sorry')
        pass
    def process_view(self,request,callback,callback_args,callback_kwargs):
        # i=1
        # print('444')
        pass

    def process_template_response(self,request,response):
        pass
    def process_exception(self,request,exception):
        print('555')
        return HttpResponse(exception)

    def process_response(self, request, response):
        # print('666')
        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        # response["Access-Control-Max-Age"] = "1000"
        # response["Access-Control-Allow-Headers"] = "*"

        return response
        # return HttpResponse('ok')