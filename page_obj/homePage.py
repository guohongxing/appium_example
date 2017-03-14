from base import Page

class homePage(Page):
	'''主页面'''
	def button_display(self,*loc):
		element = self.find_element(*loc);
		index = element.is_displayed();
		return index;

	def button_click(self,*loc):
		element = self.find_element(*loc);
		sleep(2);
		element.click();
