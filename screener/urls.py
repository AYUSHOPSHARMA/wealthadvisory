"""wealthmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from screener import views, fundamentaldataView,portfolio,fundamentalportfolioview,portfolioDetails,strategy
from django.views.decorators.cache import cache_page
from screener.FundamentalPortfolioForm import views as fundamentalview
from screener.StrategyForm import views as strategyview
from screener.MutualFund import views as mutualfundview

urlpatterns = [
         path('fundamentalData/<str:ticker>/', views.getfundamentalData),
         path('staticVR/VR/', views.getStaticVr),
         path('fundamentalDataHome/', views.fundamentalDataHome),
         #re_path(r'^fundamentalDataHome/*', fundamentaldataView.fundamentalDataHome),
         path('portfolioOptimization/', portfolio.getPortfolioChart),
         path('portfolio/', portfolio.getportfolio),
         path('portfolioPDF/', portfolio.getportfolioPDF),
         path('downloadPortfolioPDF/', portfolio.downloadPortfolioPDF),
         path('fundamentalportfolio/', fundamentalportfolioview.fundamentalportfolio),
         path('portfoliodetails/', portfolioDetails.getPortfolioDetails),
         path('portfoliolist/', portfolioDetails.getPortfolioList),
         #path('strategy/', strategy.getStrategy),
         path('inteligentstrategy/', strategyview.strategy),
         path('mutualfund/', mutualfundview.mutualfund),
          path('mutualfundajax/', mutualfundview.loadSchemeNames),
]
