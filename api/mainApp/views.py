from rest_framework import generics,mixins
from mainApp.serilizers import Chatserialier
from mainApp.models import conversations
from mainApp.faithAlgo import chat

class ChatView(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=conversations.objects.all()
    serializer_class=Chatserialier
    lookup_field='pk'

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        returned=chat(request.data.get('input_text'))
        request.data._mutable = True
        request.data.update({"response_text": returned})
        return self.create(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

MainChatListView=ChatView.as_view()