from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView


def HomeView(request):

    return render(request, 'home/landing.html')

#     template_name = 'home/landing.html'
#
# landing = HomeView.as_view()