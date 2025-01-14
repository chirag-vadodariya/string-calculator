class Calculator:
    def __init__(self):
        pass;
    
    def add(self, numbers):
        
        if numbers == "":
            return 0;
        
        numbers_string = numbers
        delimiter = ","
        
        # ceck if custom delimiter is used
        if numbers.startswith("//"):
            delimiter_end = numbers.find("\n");
            delimiter = numbers[2:delimiter_end];
            numbers_string = numbers[delimiter_end+1:];
        
        numbers_string = numbers_string.replace('\n',delimiter).strip();
        
        # check if numbers_string is empty
        if numbers_string == "":
            return 0;
        
        # check for negative numbers
        numbers_list = numbers_string.split(delimiter);
        negative_numbers = [];
        for number in numbers_list:
            if int(number) < 0:
                negative_numbers.append(number);
        if len(negative_numbers) > 0:
            raise ValueError("Negatives not allowed: " + ", ".join(negative_numbers));
        
        
        # add numbers
        sum = 0;
        for number in numbers_list:
            sum += int(number);
        return sum;
    
# calc = Calculator();
# print(calc.add("1,2,3")); # 6