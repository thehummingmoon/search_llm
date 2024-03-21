1.	import requests
2.	from bs4 import BeautifulSoup
3.	import csv
4.	
5.	API_KEY = "api_key"
6.	SEARCH_ENGINE_ID = "engine_id"
7.	RESULTS_PER_PAGE = 10  # Number of results per page
8.	NUM_PAGES = 3  # Number of pages to fetch (can be adjusted as needed)
9.	
10.	def scrape_data_from_url(url):
11.	    response = requests.get(url)
12.	    if response.status_code == 200:
13.	        soup = BeautifulSoup(response.content, 'html.parser')
14.	        title = soup.title.string.strip()
15.	        paragraphs = [p.text.strip() for p in soup.find_all('p')]
16.	        return title, "\n".join(paragraphs)
17.	    else:
18.	        print(f"Failed to fetch URL: {url}")
19.	        return None, None
20.	
21.	url = "https://www.googleapis.com/customsearch/v1"
22.	
23.	with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
24.	    fieldnames = ['Title', 'Paragraphs']
25.	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
26.	    writer.writeheader()
27.	
28.	    for page in range(NUM_PAGES):
29.	        start_index = page * RESULTS_PER_PAGE + 1
30.	        params = {
31.	            'q': "Category of Business in Vellore",
32.	            'key': API_KEY,
33.	            'cx': SEARCH_ENGINE_ID,
34.	            'lr': 'lang_en',
35.	            'gl': 'US',
36.	            'start': start_index
37.	        }
38.	        response = requests.get(url, params=params)
39.	        results = response.json().get('items', [])
40.	
41.	        print(f"Page {page + 1}:")
42.	        for item in results:
43.	            url = item['link']
44.	            title, paragraphs = scrape_data_from_url(url)
45.	            if title:
46.	                print("Title:", title)
47.	            if paragraphs:
48.	                print("Paragraphs:", paragraphs)
49.	                writer.writerow({'Title': title, 'Paragraphs': paragraphs})
50.	            print()
