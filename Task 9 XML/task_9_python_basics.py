import os
import sys
import csv
import json
import string
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta



class News:
    def __init__(self, text, city, date=None):
        self.text = text
        self.city = city
        self.date = date if date else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def publish(self):
        with open('News.txt', 'a', encoding='utf-8') as file:
            file.write('\nNews:\n')
            file.write(f'{self.text}\n')
            file.write(f'Issued city: {self.city}\tDate of post: {self.date}\n')


class Advertisement:
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
        self.days_left = (self.expiration_date - datetime.now()).days

    def publish(self):
        with open('News.txt', 'a', encoding='utf-8') as file:
            file.write('\nAdvertisement:\n')
            file.write(f'{self.text}\n')
            file.write(f'Actual until: {self.expiration_date.date()}, {self.days_left} days left\n')


class MyPost:
    def __init__(self, user_name, text, date_of_post=None):
        self.user_name = user_name
        self.text = text
        self.date_of_post = date_of_post if date_of_post else datetime.today().strftime('%d-%m-%Y')

    def publish(self):
        with open('News.txt', 'a', encoding='utf-8') as file:
            file.write('\nMy_post:\n')
            file.write(f'Publisher name: {self.user_name}\tDate of post: {self.date_of_post}\n')
            file.write(f'{self.text}\n')


class FileReader:
    def __init__(self, input_file=None, output_file=None):
        self.input_file = input_file or f'{sys.path[0]}\\News.txt'
        self.output_file = output_file or f'{sys.path[0]}\\Processed_News.txt'

    def read_file_with_items(self) -> str:
        if not os.path.exists(self.input_file):
            return f"Error: File '{self.input_file}' not found."

        with open(self.input_file, 'r', encoding='utf-8') as file:
            text = file.read().strip()

        if "News:" in text or "Advertisement:" in text or "My post:" in text:
            return text
        else:
            return "Format mismatch!"

    def write_file_from_another(self, text: str) -> None:
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(text + '\n\n')
        print(f"Data successfully written to '{self.output_file}'")

    def delete_input_file(self) -> None:
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
            print(f"File '{self.input_file}' has been deleted.")
        else:
            print(f"Error: File '{self.input_file}' not found.")


class CsvProcessor:
    def __init__(self, output_word_file='word_counter.csv', output_detail_file='detailed_counter.csv'):
        self.output_word_file = output_word_file
        self.output_detail_file = output_detail_file

    def word_counter(self, text: str) -> None:
        with open(self.output_word_file, 'w', encoding='utf-8') as word_counter:
            writer = csv.writer(word_counter, delimiter='-')
            words = list(set(text.lower().split()))
            for word in words:
                writer.writerow([f'{word}', f'{text.lower().count(word)}'])
        print(f"Word count written to '{self.output_word_file}'")

    def detailed_counter(self, text: str) -> None:
        with open(self.output_detail_file, 'w', encoding='utf-8') as detailed_counter:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(detailed_counter, fieldnames=headers)
            writer.writeheader()
            for char in string.ascii_lowercase:
                writer.writerow({
                    'letter': char,
                    'count_all': text.lower().count(char),
                    'count_uppercase': text.count(char.upper()),
                    'percentage': round(text.lower().count(char) * 100 / len(text), 2)
                })
        print(f"Detailed count written to '{self.output_detail_file}'")


class JsonProcessor:
    def __init__(self, json_file='C:\\Users\\anastasiya_shyshliuk\\PycharmProjects\\python_course\\Task 8 JSON\\file_to_input.json'):
        self.json_file = json_file

    def json_schema_validator(self):
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                json_data = json.load(file)

            text_to_process = ""

            if sorted(json_data.keys()) == sorted(['type', 'text', 'city', 'date_of_post']):
                news = News(json_data['text'], json_data['city'], json_data['date_of_post'])
                news.publish()
                text_to_process = json_data['text']
            elif sorted(json_data.keys()) == sorted(['type', 'text', 'expiration_date']):
                ad = Advertisement(json_data['text'], json_data['expiration_date'])
                ad.publish()
                text_to_process = json_data['text']
            elif sorted(json_data.keys()) == sorted(['type', 'user_name', 'text', 'date_of_post']):
                post = MyPost(json_data['user_name'], json_data['text'], json_data['date_of_post'])
                post.publish()
                text_to_process = json_data['text']
            else:
                print('Error: Incorrect file structure!')
                return


            csv_processor = CsvProcessor()
            csv_processor.word_counter(text_to_process)
            csv_processor.detailed_counter(text_to_process)

            print("JSON data processed successfully.")

        except json.JSONDecodeError:
            print("Error: Failed to decode JSON file.")
        except FileNotFoundError:
            print(f"Error: File '{self.json_file}' not found.")

    def remove_json(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
            print(f"JSON file '{self.json_file}' has been deleted.")
        else:
            print(f"Error: JSON file '{self.json_file}' not found.")


json_processor = JsonProcessor(json_file='C:\\Users\\anastasiya_shyshliuk\\PycharmProjects\\python_course\\Task 9 JSON\\file_to_input.json')
json_processor.json_schema_validator()
json_processor.remove_json()

file_processor = FileReader(input_file="News.txt")
content = file_processor.read_file_with_items()

if content != "Format mismatch!" and not content.startswith("Error"):
    file_processor.write_file_from_another(content)
    file_processor.delete_input_file()
else:
    print(content)

csv_processor = CsvProcessor()
with open('Processed_News.txt', 'r', encoding='utf-8') as file:
    processed_text = file.read()

csv_processor.word_counter(processed_text)
csv_processor.detailed_counter(processed_text)


class XmlProcessor:
    def __init__(self, xml_file=r'C:\Users\anastasiya_shyshliuk\PycharmProjects\python_course\Task 9 XML\file_to_input.xml'):
        self.xml_file = xml_file

    def xml_schema_validator(self):
        try:
            tree = ET.parse(self.xml_file)
            root = tree.getroot()
            tags = {child.tag for child in root}
            text_to_process = ""

            if tags == {'type', 'text', 'city', 'date_of_post'}:
                news = News(root.find('text').text, root.find('city').text, root.find('date_of_post').text)
                news.publish()
                text_to_process = root.find('text').text
            elif tags == {'type', 'text', 'expiration_date'}:
                expiration_date = (datetime.now() + timedelta(days=int(root.find('days_to_expire').text))).strftime(
                    '%Y-%m-%d')
                ad = Advertisement(root.find('text').text, expiration_date)
                ad.publish()
                text_to_process = root.find('ad_text').text
            elif tags == {'type', 'user_name', 'text', 'date_of_post'}:
                post = MyPost(root.find('user_name').text, root.find('text').text, root.find('date_of_post').text)
                post.publish()
                text_to_process = root.find('post_text').text
            else:
                print("Error: Incorrect XML structure!")
                return

            file_processor = FileReader(input_file="News.txt")
            content = file_processor.read_file_with_items()
            if content != "Format mismatch!" and not content.startswith("Error"):
                file_processor.write_file_from_another(content)
                file_processor.delete_input_file()
            else:
                print(content)


            csv_processor = CsvProcessor()
            csv_processor.word_counter(text_to_process)  # Передаем текст
            csv_processor.detailed_counter(text_to_process)

            print("XML data processed successfully.")
        except ET.ParseError:
            print("Error: Failed to parse XML file.")
        except FileNotFoundError:
            print(f"Error: File '{self.xml_file}' not found.")

    def remove_xml(self):
        if os.path.exists(self.xml_file):
            os.remove(self.xml_file)
            print(f"XML file '{self.xml_file}' has been deleted.")
        else:
            print(f"Error: XML file '{self.xml_file}' not found.")


xml_processor = XmlProcessor()
xml_processor.xml_schema_validator()
xml_processor.remove_xml()

file_processor = FileReader(input_file="News.txt")
content = file_processor.read_file_with_items()

if content != "Format mismatch!" and not content.startswith("Error"):
    file_processor.write_file_from_another(content)
    file_processor.delete_input_file()
else:
    print(content)


with open("Processed_News.txt", "r", encoding="utf-8") as file:
    processed_text = file.read()


csv_processor = CsvProcessor()
csv_processor.word_counter(processed_text)
csv_processor.detailed_counter(processed_text)