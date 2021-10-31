# Using Python to Access Web Data
The repo contains code for excercises completed by me during University of Michigan ["Using Python to Access Web Data"](https://www.coursera.org/learn/python-network-data?specialization=python) class.

Course description on Coursera:

*This course will show how one can treat the Internet as a source of data.  We will scrape, parse, and read web data as well as access data using web APIs.  We will work with HTML, XML, and JSON data formats in Python.  This course will cover Chapters 11-13 of the textbook “Python for Everybody”. To succeed in this course, you should be familiar with the material covered in Chapters 1-10 of the textbook and the first two courses in this specialization.  These topics include variables and expressions, conditional execution (loops, branching, and try/except), functions, Python data structures (strings, lists, dictionaries, and tuples), and manipulating files.  This course covers Python 3.*

## List of files and folders:

1. **Finding numbers**: a script (1_finding_numbers.py) and data to run the script on (1_finding_numbers.txt, [source](http://py4e-data.dr-chuck.net/)). The script reads through and parses a file with text and numbers, extracts all the numbers in the file, and computes their sum. 
2. **Exploring HTTP**: a script (2_exploring_HTTP.py) retrieves a URL, and prints out the headers and data.
3. **Scraping HTML data**: a script (3_scraping_HTML_data.py) reads the HTML from a URL, parses the data using BeautifulSoup, extracts numbers and compute the sum of the numbers in the file. 
4. **Following links in HTML**: a script (4_following_links_in_HTML.py) uses urllib to read the HTML from a URL, extracts the href= values from the anchor tags, scans for a tag that is in a particular position from the top and follow that link, repeats the process a number of times, and report the last name it finds.
5. **Extracting Data from XML**: a script (5_extracting_data_from_XML.py) prompts for a URL, reads the XML data from that URL using urllib, parses and extracts the comment counts from the XML data, and computes the sum of the numbers in the file. 
6. **Extracting Data from JSON**: a script (6_extracting_data_from_JSON.py) prompts for a URL, reads the JSON data from that URL using urllib, parses and extracts the comment counts from the JSON data, and computes the sum of the numbers in the file.
7. **Using the GeoJSON API**: a script (7_using_the_GeoJSON_API.py) prompts for a location, contacts a web service and retrieves JSON for the web service, parses that data, and retrieves the first place_id (a textual identifier that uniquely identifies a place as within Google Maps) from the JSON.  
