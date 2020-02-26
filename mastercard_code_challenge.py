from dictor import dictor
import requests
import collections


def required_inputs():

	page_id = input("Input Page ID (E.g - 2172104):")

	no_top_results = input("Input number of top word results (E.g - 5):")

	code_challenge(page_id, no_top_results)


def code_challenge(page_id, no_top_results):

	if page_id == "":
		print("Please input valid page id!")
		required_inputs()

	try:
		final_no_top_results = int(no_top_results)
	except ValueError as e:
		print(f"Please input valid number! ERROR: {e}")
		return

	page_url_string = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={page_id}0&explaintext&format=json"
	r = requests.get(page_url_string)
	status = r.status_code
	connection_check(status, r, page_id, final_no_top_results)


def connection_check(status, data, page_id, final_no_top_results):

	if status == 200:
		information_extraction(data, page_id, final_no_top_results)
	elif status == 404:
		print("Response Fail")
		required_inputs()


def information_extraction(data, page_id, final_no_top_results):

	response = data.json()

	print("URL:")
	print(data.url)
	for key, values in response.items():
		if key == 'query':
			print("Page Title: " + str(dictor(response, f"query.pages.{page_id}0.title")))

	component = ""
	component_list = []

	for each in data.text:

		if each != '"' and each != ' ' and each.isalnum():
			component += each
		if each == '"' or each == ' ':
			component_list.append(component)
			component = ""

	for each in component_list:
		if each == '':
			component_list.remove(each)

	c = collections.Counter(component_list)

	print(f"Top {final_no_top_results} Words:")
	for key, values in c.most_common(final_no_top_results):
		print("- " + str(values), str(key))


if __name__ == '__main__':
	required_inputs()
