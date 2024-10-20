import requests
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Profile, Lang, Project, Edu, Work, Contact, Credit
from bs4 import BeautifulSoup


def Scraper():
    USER_AGENT = 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    cnt = session.get("https://www.hackerrank.com/leroyjeslyn").text
    return cnt


# Create your views here.
def home(request):
    prof = Profile.objects.get(Acct_id=1)
    edu = Edu.objects.filter(Acct_id=1).order_by('-id')
    work = Work.objects.filter(Acct_id=1).order_by('-id')
    lang = Lang.objects.filter(Acct_id=1)
    proj = Project.objects.filter(Acct_id=1)

    # r = Scraper()
    # soup = BeautifulSoup(r, 'html.parser')
    # souper = soup.find_all('div', {'class': 'ui-badge-wrap'})
    # for img in souper:
    #     imgs.append(img)

    ctx = {
        # "Badges": list(enumerate(imgs))[::-1],
        "Prof": prof,
        "Edu": edu,
        "Work": work,
        "Langs": lang,
        "Projs": proj,
        "Els": ["About Me", "Work Experience", "Projects", "Education"],
    }

    return render(request, "Home.html", ctx)


def test(request):
    nop = 400 # Number of Particles
    lst = [0] * nop
    return render(request, "Test.html", {"Lst": lst})
