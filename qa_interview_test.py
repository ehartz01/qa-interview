from seleniumbase import BaseCase
import time

class MyTestClass(BaseCase):
	def test_basics(self):
		self.open("https://github.com/")
		# after landing on the main page, search "react" in the search bar
		self.type('input[type="text"]', 'react')
		self.submit('input[type="text"]')
		time.sleep(2)
		# click on the filter dropdown to go through different filters and perform some tesing.
		for i in range(4,9):
			self.click_nth_visible_element('a[class="menu-item"]', i)
			time.sleep(1)
		# # clear the filter and go to facebook/react repo and verify some page elements
		self.click_nth_visible_element('a[class="menu-item"]', 0)
		self.click('a[href="/facebook/react"]') #occasionally fails

		# navigate through different tabs of the repo (e.g. Issues, Pull requests, etc.)
		for tabid in ["issues-tab", "pull-requests-tab", "actions-tab", "projects-tab", "wiki-tab", "code-tab"]:
			self.click(f'a#{tabid}')
			time.sleep(1)
		self.click('a#code-tab')
		# hover over on the main navigation and verify the dropdown content (e.g. Product, Solutions, etc)
		self.hover('button[class*="HeaderMenu-link"]:contains("Product")')
		self.assert_element('a:contains("Actions")')
		self.hover('button[class*="HeaderMenu-link"]:contains("Solutions")')
		self.assert_element('a:contains("Enterprise")')
		self.hover('button[class*="HeaderMenu-link"]:contains("Open Source")')
		self.assert_element('a:contains("Topics")')
		## Extra ##
		## write any tests you find interesting, don't go too wild :)
		self.click('summary[class="btn-primary btn"]')
		self.click('button:contains("Codespaces")')
