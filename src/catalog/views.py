from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product
from django.views.generic import TemplateView, RedirectView
# Import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class CatalogPageView(TemplateView):
    template_name = "primes/catalog.html"

    """def show_category(request, category_slug, template_name="category.html"):
        c = get_object_or_404(Category, slug=category_slug)
        products = c.product_set.all()
        page_title = c.name
        meta_keywords = c.meta_keywords
        meta_description = c.meta_description
        return render(template_name, locals(), context_instance=RequestContext(request))

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.update_counter()
        return super(ArticleCounterRedirectView, self).get_redirect_url(*args, **kwargs)"""

class ProductPageView(TemplateView):
    template_name = "catalog/product.html"

    """def show_product(request, product_slug, template_name="product.html"):
        p =get_object_or_404(Product, slug=product_slug)
        categories = p.categories.filter(is_active=True)
        page_title = p.name
        meta_keywords = p.meta_keywords
        meta_description = p.meta_description
        return render(template_name, locals(), context_instance=RequestContext(request))"""

class AboutPageView(TemplateView):
    template_name = "about.html"

class CategoryPageView(TemplateView):
    template_name = "catalog/category.html"


