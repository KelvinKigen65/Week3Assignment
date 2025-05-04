
with open("input.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Here is the second line.\n")
    file.write("Python makes file handling easy.\n")
    file.write("Let's count the words in this file.\n")
    file.write("This is the final line in the text.\n")
with open("input.txt", "r") as file:
    content = file.read()

word_count = len(content.split())

uppercase_content = content.upper()

with open("output.txt", "w") as file:
    file.write(uppercase_content + "\n")
    file.write(f"Word Count: {word_count}\n")

print("Processing complete! The transformed text and word count are saved in 'output.txt'.")
