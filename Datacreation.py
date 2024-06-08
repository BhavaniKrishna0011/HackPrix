import random, time

def generate_random_data(file_path):
    # Define the patterns for types and URLs
    types = ['clothing', 'sports', 'vehicle']
    urls = ['http://example.com/image1.jpg', 'http://example.com/image2.jpg', 'http://example.com/image3.jpg']

    # Generate random data
    random_data = []
    data_type = random.choice(types)
    url = random.choice(urls)
    random_data.append(f"{data_type},{url}")

    # Save data to file
    with open(file_path, 'w') as file:
        for data in random_data:
            file.write(data + '\n')

def main():
    # Specify the file path
    file_path = 'temp_data.txt'

    # Generate and save random data
    generate_random_data(file_path)
    print("Random data saved to:", file_path)

if __name__ == "__main__":
    for i in range(1,100):
        time.sleep(2)
        main()
