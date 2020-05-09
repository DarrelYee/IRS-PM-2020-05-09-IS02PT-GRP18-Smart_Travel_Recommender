from boilerpy3 import extractors

while(1):
    try:
        URL = input()
        if URL == "exit": break
        extractor = extractors.DefaultExtractor()
        content = extractor.get_content_from_url(URL)
    except:
        print("Error visiting URL, skipping...")
