import statistics

# Recursive function to count digits in an integer
def count_digits(n):
  if n == 0:
    return 0
  return 1 + count_digits(n // 10)

# Recursive function to find the maximum value in a list
def find_max(numbers):
    if not numbers:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    else:
        return max(numbers[0], find_max(numbers[1:]))

# Recursive function to count occurrences of a tag in HTML code
def count_tags(html, tag):
    open_tag = f"<{tag}>"
    close_tag = f"</{tag}>"
    if open_tag in html:
        return 1 + count_tags(html[html.find(open_tag) + len(open_tag):], tag)
    else:
        return 0

# Recursive function to count normalized columns in a 2D matrix
def count_normalized_columns(matrix, col_index):
    if col_index == len(matrix[0]):
        return 0
    column_values = [matrix[row][col_index] for row in range(len(matrix))] 
    if statistics.mean(column_values) == 0 and statistics.stdev(column_values) == 1:
        return 1 + count_normalized_columns(matrix, col_index + 1)
    else:
        return count_normalized_columns(matrix, col_index + 1)

# Main menu
def main():
    while True:
        print("- - - - - - - - - - - - - - -")
        print("1. Count Digits")
        print("2. Find Max")
        print("3.1. Count Tags (HTML)")
        print("3.2. Count Normalized Columns")
        print("4. Exit")
        choice = input("Enter a choice: ")

        if choice == "1":
            n = int(input("Enter an integer: "))
            digit_count = count_digits(abs(n))
            print(f"Output: {digit_count}")
        elif choice == "2":
            numbers = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
            if not numbers:
                print("Output: 0")
            else:
                max_result = find_max(numbers)
                print(f"Output: {max_result}")
        elif choice == "3.1":
            html = """<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>"""
            tag = input("Enter a tag: ")
            tag_count = count_tags(html, tag)
            print(f"Output: {tag_count}")
        elif choice == "3.2":
            matrix = [ [-1.2649110640673518, 5.123451, 43],
          [-0.6324555320336759, 5.13123123, 4334],
          [0.0, 6.1543453, 125879],
          [0.6324555320336759, 0.1231235709, 123544],
          [1.2649110640673518, 9.1543524234, 55676] ]
            normalized_columns = count_normalized_columns(matrix, 0)
            print(f"The number of normalized columns is: {normalized_columns}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 
