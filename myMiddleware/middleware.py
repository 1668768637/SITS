class myMiddleware:
   # middleware_name:中间件的名字

   def __init__(self, get_response):
       # 初始化中间件,项目启动时会进行初始化
       print('项目启动了')
       # get_response这是固定的写法(一般都这样写)
       self.get_response = get_response
       #self.str = '你可以在这里初始化一写参数'

   def __call__(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print('ip:', ip)
        #print(self.str)  # 也可以使用init中初始化的参数
        response = self.get_response(request)
        return response
