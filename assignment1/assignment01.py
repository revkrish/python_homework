def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!" #f is used to format the string with the variable name

def calc(num1, num2, operation="multiply"):
    if operation == "multiply":
        try:
            return num1 * num2
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        if num2 == 0:
            return "You can't divide by 0!"
        else:
            return num1 / num2
    elif operation == "int_divide":
        if num2 == 0:
            return "You can't divide by 0!"
        else:
            return num1 // num2
    elif operation == "modulo":
        return num1 % num2
    elif operation == "power":
        return num1 ** num2
    else:
        return f"Unsupported operation: {operation}"

def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return f"Invalid target type: {target_type}"
    except ValueError:
        return f"You can't convert {value} into a {target_type}."


def grade(*scores):
    try:
        if not scores:
            return "Invalid data was provided."
        average = sum(scores) / len(scores)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

def repeat(string, times):
    result = ""
    for _ in range(times):
        result += string
    return result

def student_scores(statistic, **scores):
    if statistic == "mean":
        return sum(scores.values()) / len(scores)
    elif statistic == "best":
        return max(scores, key=scores.get)          

def titleize(string):
    little_words = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor", "of", "on", "or", "per", "the", "to"}
    words = string.split()
    titled_words = []
    for i, word in enumerate(words):
        if i > 0 and word.lower() in little_words:
            titled_words.append(word.lower())
        else:
            titled_words.append(word.capitalize())
    return " ".join(titled_words)

def hangman(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def pig_latin(sentence):
    def convert_word(word):
        vowels = "aeiou"
        if word[0] in vowels:
            return word + "ay"
        if word[:2].lower() == "qu":
            return word[2:] + word[:2] + "ay"
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"

    words = sentence.split()
    return ' '.join(convert_word(word) for word in words) 

def main():
    print(hello())
    greet("James")
    print(calc(5, 6))
    print(calc(5, 6, "add"))
    print(calc(20, 5, "divide"))
    print(calc(14, 2.0, "multiply"))
    print(calc(12.6, 4.4, "subtract"))
    print(calc(9, 5, "modulo"))
    print(calc(10, 0, "divide"))
    print(calc("first", "second", "multiply"))
    print(data_type_conversion("110", "int"))
    print(data_type_conversion("5.5", "float"))
    print(data_type_conversion(7,"float"))
    print(data_type_conversion(91.1,"str"))
    print(data_type_conversion("banana", "int"))
    print(grade(75,85,95))
    print(grade("three", "blind", "mice"))
    print(repeat("up,", 4))
    print(student_scores("mean", Tom=75, Dick=89, Angela=91))
    print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50 ))
    print(titleize("war and peace"))
    print(titleize("a separate peace"))
    print(titleize("after on"))
    print(hangman("difficulty","ic"))
    print(pig_latin("apple"))
    print(pig_latin("banana"))
    print(pig_latin("cherry"))
    print(pig_latin("quiet"))
    print(pig_latin("square"))
    print(pig_latin("the quick brown fox"))


if __name__ == "__main__":
    main()  

