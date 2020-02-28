from dictor import dictor
import requests
import collections
import yaml


def required_inputs():

	page_id = input("Input Page ID (E.g - 2172104):")
	no_top_results = input("Input number of top word results (E.g - 5):")
	information_check(page_id, no_top_results)


def information_check(page_id, no_top_results):

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

	if connection_check(status):
		information_extraction(r, page_id, final_no_top_results)
	else:
		print("Response Fail")
		required_inputs()


def connection_check(status):

	status_string = str(status)

	if str(status_string[0]) == '2':
		return True
	else:
		return False


def information_extraction(data, page_id, final_no_top_results):

	response = data.json()

	final_information_dict = {}
	final_information_dict['URL'] = data.url

	final_information_dict["Title"] = dictor(response, f"query.pages.{page_id}0.title")
	extraction = dictor(response, f"query.pages.{page_id}0.extract")

	component = ""
	component_list = []

	for each in extraction:
		if each != '"' and each != ' ' and each.isalnum():
			component += each
		if each == '"' or each == ' ':
			component_list.append(component)
			component = ""

	for each in component_list:
		if each == '':
			component_list.remove(each)

	c = collections.Counter(component_list)

	final_key = f"Top {final_no_top_results} Words"

	final_information_dict[final_key] = {}

	for key, values in c.most_common(final_no_top_results):
		final_information_dict[final_key][values] = key

	yaml_final_view(final_information_dict)


def yaml_final_view(final_dict):
	print('-------------------------------')
	print(yaml.dump(final_dict, default_flow_style=False, sort_keys=False))


if __name__ == '__main__':
	required_inputs()
