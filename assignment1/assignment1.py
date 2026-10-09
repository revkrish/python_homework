def hello():
    return "Hello!"

def greet(name):
    print(f"Hello, {name}!")

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
    elif operation == "modulo":
        return num1 % num2  

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


def grade(score1, score2, score3):  
    try:
        average = (score1 + score2 + score3) / 3
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
    return string * times

def student_scores(statistic, **scores):
    if statistic == "mean":
        return sum(scores.values()) / len(scores)
    elif statistic == "best":
        return max(scores, key=scores.get)          

def titleize(string):
    return string.title()

def hangman(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def pig_latin(sentence):
    def convert_word(word):
        vowels = "aeiou"
        if word[0] in vowels:
            return word + "ay"
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    return word[i:] + word[:i] + "ay"
            return word + "ay"  # For words without vowels

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

