from datetime import datetime

class News:
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = datetime.now()

    def publish(self):
        with open('News.txt', 'a') as file:
            file.write('\n')
            file.write('\nNews: \n')
            file.write(self.text + '\n')
            file.write(f'Issued city: {self.city} \t Date_of_post: {self.date} \n\n')


class Advertisement:
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, '%d/%m/%Y')
        self.days_left = (self.expiration_date - datetime.now()).days

    def publish(self):
        with open('News.txt', 'a') as file:
            file.write('\n')
            file.write('\nAdvertisement: \n')
            file.write(self.text + '\n')
            file.write('Actual until: ' + str(self.expiration_date.date()))
            file.write(', ' + str(self.days_left) + ' days left')


class MyPost:
    def __init__(self, user_name, text):
        self.user_name = user_name
        self.text = text
        self.date_of_post = datetime.today().strftime('%d-%m-%Y')

    def publish(self):
        with open('News.txt', 'a') as file:
            file.write('\n')
            file.write('\nMy post: \n')
            file.write(f'Publisher name: {self.user_name} \t Date_of_post: {self.date_of_post} \n\n')
            file.write(self.text + '\n')


def main():
    while True:
        print("\Choose an option to add:")
        print("1. News")
        print("2. Advertisement")
        print("3. My Post")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            text = input('Enter the news text: ')
            city = input('Enter the city: ')
            news = News(text, city)
            news.publish()
            print("News publish successfully!")

        elif choice == '2':
            text = input("Enter the advertisement text: ")
            expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
            try:
                ad = Advertisement(text, expiration_date)
                ad.publish()
                print("Advertisement published successfully!")
            except ValueError:
                print("Invalid date format. Please try again.")

        elif choice == '3':
            user_name = input("Enter your name: ")
            text = input("Enter your post text: ")
            post = MyPost(user_name, text)
            post.publish()
            print("Post published successfully!")

        elif choice == '4':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4")

if __name__ == "__main__":
    main()