def remove_duplicates(file_path):
    unique_urls = set()

    # Read URLs from the file and add them to a set to remove duplicates
    with open(file_path, "r") as file:
        urls = file.readlines()
        for url in urls:
            unique_urls.add(url.strip())

    # Write unique URLs back to the file
    with open(file_path, "w") as file:
        for url in unique_urls:
            file.write(url + "\n")


def main():
    file_path = "././data/discovered_urls.txt"
    remove_duplicates(file_path)
    print("Duplicates removed from the file:", file_path)


if __name__ == "__main__":
    main()
