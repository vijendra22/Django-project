from django.template import loader
from .models import Page
from django.http import HttpResponse
from django.http import Http404

def home_to_all(request):
    #return HttpResponse("Welcome, to home page.")
    #return render_to_response('Home/home_page.html')
    all_pages = Page.objects.all()
    template = loader.get_template('Home/index.html')
    context = {
        'all_pages': all_pages,
    }
    return HttpResponse(template.render(context, request))


def in_page(request, page_num):
    try:

        if(page_num == 1):
            template = loader.get_template('Home/index.html')
        if (page_num == 2):
            template = loader.get_template('Home/gettingdjango.html')
        if (page_num == 3):
            template = loader.get_template('Home/collection.html')
        if (page_num == 4):
            template = loader.get_template('Home/tutorial1.html')
        if (page_num == 5):
            template = loader.get_template('Home/tutorial2.html')
        if (page_num == 6):
            template = loader.get_template('Home/tutorial3.html')
        if (page_num == 7):
            template = loader.get_template('Home/tutorial4.html')
        if (page_num == 8):
            template = loader.get_template('Home/tutorial5.html')
        if (page_num == 9):
            template = loader.get_template('Home/tutorial6.html')
        if (page_num == 10):
            template = loader.get_template('Home/aboutwebsite.html')
        if (page_num == 11):
            template = loader.get_template('Home/aboutme.html')
        if (page_num == 12):
            template = loader.get_template('Home/help.html')
        if (page_num == 13):
            template = loader.get_template('Home/officialwebsite.html')

        page = Page.objects.get(pk=page_num)
    except Page.DoesNotExist:
        raise Http404("Page does not Exist...")
    return HttpResponse(template.render({'page': page}, request))
