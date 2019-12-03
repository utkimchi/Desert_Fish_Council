from __future__ import print_function
import csv , json , boto3

csvpath = 'sub_t.csv'

jsonpath = 'sub_JS.json'

data = {}

with open(csvpath, encoding = "utf8") as csvFile:
	csvReader = csv.DictReader(csvFile)
	for rows in csvReader:
		id = rows['#']
		data[id] = rows

with open(jsonpath, 'w') as jsonFile:
	jsonFile.write(json.dumps(data, indent=2))

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('dfc_t2')

with open(jsonpath) as jsonUpload:
	submissions = json.load(jsonUpload)
	for key,sub in submissions.items():
		tid = sub['#']
		title = sub['title']
		author = sub['authors']
		submitted = sub['submitted']
		last_update = sub['last updated']
		form_fields = sub['form fields']
		keywords = sub['keywords']
		decision = sub['decision']
		notified = sub['notified']
		revssent = sub['reviews sent']
		abstract = sub['abstract']
		print("Adding sub" , tid , title)
		print(table.creation_date_time)
		table.put_item(
			Item={
				'#':tid,
				'title':title,
				'authors':author,
				'submitted':submitted,
				'last updated':last_update,
				'form fields':form_fields,
				'keywords':keywords,
				'decisions':decision,
				'notified':notified,
				'reviews sent':revssent,
				'abstract':abstract,
			})
