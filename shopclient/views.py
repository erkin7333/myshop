from django.shortcuts import render
from django.views.generic import TemplateView
from shopcabinet.models import Category, Setting, Post


class IndexView(TemplateView):
    template_name = "shopclient/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        side = map(int, Setting.objects.get(key="main_side_categories").value.split(","))
        context['sidebar_menu'] = Category.objects.filter(id__in=side).all()
        return context


class MainCategory(TemplateView):
    template_name = 'shopclient/category.html'


class AboutPage(TemplateView):
    template_name = 'shopclient/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        post = Post.objects.all()
        context['post'] = post
        return context


# class ContactPage(TemplateView):
#     template_name = 'shopclient/contact.html'
#     extra_context = {
#         'contact': Post.objects.get(id=2)
#     }