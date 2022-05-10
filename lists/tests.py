from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.http import render
from django.http import HttpResponse

from lists.views import home_page


class HomePageTest(TestCase):
	def home_page(request):
		return render(request,'home.html',{
			'new_item_text':request.POST.get('item_text',''),
			})	


	def test_uses_home_template(self):
		response=self.client.get('/')
		self.assertTemplateUsed(response,'home.html')


    def test_can_save_a_POST_request(self):
        response=self.client.post('/',data={'item_text': 'A new list item'})
        self.assertIn('A new list item',response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

