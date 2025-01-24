import os
import sys
import csv
import string
from datetime import datetime


class News:
    def __init__(self, text, city, date=None):
        self.text = text
        self.city = city
        self.date = date if date else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def publish(self):
        with open('News.txt', 'a') as file:
            file.write('\nNews:\n')
            file.write(f'{self.text}\n')
            file.write(f'Issued city: {self.city}\tDate of post: {self.date}\n')


class Advertisement:
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
        self.days_left = (self.expiration_date - datetime.now()).days

    def publish(self):
        with open('News.txt', 'a') as file:
            file.write('\nAdvertisement:\n')
            file.write(f'{self.text}\n')
            file.write(f'Actual until: {self.expiration_date.date()}, {self.days_left} days left\n')


class MyPost:
    def __init__(self, user_name, text, date_of_post=None):
        self.user_name = user_name
        self.text = text
        self.date_of_post = date_of_post if date_of_post else datetime.today().strftime('%d-%m-%Y')

    def publish(self):
        with open('News.txt', 'a') as file:
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
        with open(self.output_file, 'a', encoding='utf-8') as file:
            file.write(text + '\n\n')
        print(f"Data successfully written to '{self.output_file}'")

    def delete_input_file(self) -> None:
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
            print(f"File '{self.input_file}' has been deleted.")
        else:
            print(f"Error: File '{self.input_file}' not found.")


class CsvProcessor:
    def __init__(self, input_file='Task 6 Module/Processed_News.txt', output_word_file='Task 7 csv/word_counter.csv',
                 output_detail_file='Task 7 csv/detailed_counter.csv'):
        self.input_file = input_file
        self.output_word_file = output_word_file
        self.output_detail_file = output_detail_file

    def word_counter(self) -> None:
        with open(self.input_file, 'r', encoding='utf-8') as file_reader:
            reader = file_reader.read()

        with open(self.output_word_file, 'w', encoding='utf-8') as word_counter:
            writer = csv.writer(word_counter, delimiter=' ')
            words = list(set(reader.lower().split()))
            for word in words:
                writer.writerow([f'{word}', f'{reader.lower().count(word)}'])
        print(f"Word count written to '{self.output_word_file}'")

    def detailed_counter(self) -> None:
        with open(self.input_file, 'r', encoding='utf-8') as file_reader:
            reader = file_reader.read()

        with open(self.output_detail_file, 'w', encoding='utf-8') as detailed_counter:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(detailed_counter, fieldnames=headers)
            writer.writeheader()
            for char in string.ascii_lowercase:
                writer.writerow({
                    'letter': char,
                    'count_all': reader.lower().count(char),
                    'count_uppercase': reader.count(char.upper()),
                    'percentage': round(reader.lower().count(char) * 100 / len(reader), 2)
                })
        print(f"Detailed count written to '{self.output_detail_file}'")


csv_processor = CsvProcessor()
csv_processor.word_counter()
csv_processor.detailed_counter()


