from django.contrib.syndication.views import Feed  
from django.template.defaultfilters import truncatewords  
from .models import Advert 
  
  
class LatestAdvertFeed(Feed):  
    title = 'advert'  
    link = '/advert/'  
    description = 'New advert of my site.'  
    def items(self):  
            return Advert.objects.order_by('-created')[:5]  
      
    def item_title(self, item):  
        return item.subject  
      
    def item_description(self, item):  
        return truncatewords(item.description, 10)