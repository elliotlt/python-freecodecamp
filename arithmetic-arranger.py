def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes = ""
    results = ""
    
    for i in problems:
        num1, operator, num2 = i.split()
        
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(num1), len(num2)) + 2
        
        # rjust() right-aligns the text within the given width
        first_line += num1.rjust(width) + "    "
        second_line += operator + num2.rjust(width - 1) + "    "
        dashes += "-" * width + "    "
        
        if show_answers:
            # eval() evaluates the string expression (e.g., "123 + 49" becomes 172)
            result = str(eval(i))
            results += result.rjust(width) + "    "
    
    # rstrip() removes trailing whitespace from the string
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip()
    if show_answers:
        arranged_problems += "\n" + results.rstrip()
    
    return arranged_problems


print(arithmetic_arranger(["8777 - 8", "100 - 43", "123 + 49", "888 + 40", "653 + 87"], True)
