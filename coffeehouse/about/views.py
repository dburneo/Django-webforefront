from django.shortcuts import render
from coffeehouse.stores.views import STORE_LIST
from django.http import Http404, HttpResponse
from django.views.generic import View


def index(request, store_id=None):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    if store_id == None:
        store = STORE_LIST[0]
    elif store_id == '1':
        store = STORE_LIST[1]
    elif store_id == '2':
        store = STORE_LIST[2]
    elif store_id == '3':
        store = STORE_LIST[3]
    else:
        raise Http404
    return render(request, 'about/index.html', {'store':store})


class ContactPage(View):
    mytemplate = 'about/contact.html'
    unsupported = 'Unsopported operation'

    def get(self, request, store_id=None):
        # Create fixed data structures to pass to template
        # data could equally come from database queries
        if store_id == None:
            store = STORE_LIST[0]
        elif store_id == "1":
            store = STORE_LIST[1]
        elif store_id == "2":
            store = STORE_LIST[2]
        elif store_id == "3":
            store = STORE_LIST[3]
        else:
            raise Http404
        return render(request, self.mytemplate, {'store':store})

    def post(self, request):
        return HttpResponse(self.unsupported)
