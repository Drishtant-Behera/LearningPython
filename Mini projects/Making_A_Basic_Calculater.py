num_1 = int(input("first number:"))num_2 = int(input("second number:"))adding_process = num_1 + num_2subtracting_process = num_1 - num_2multiplying_process = num_1 * num_2dividing_process = num_1 / num_2adding_example = ("In adding you have to give (+)")subtracting_example = ("In subtracting you have to give (-)")multiplying_example = ("In multiplying you have to give (*) or (x)")dividing_example = ("In dividing you have to give (/)")operator = input("what operation do you want to do/nFor example/n", adding_example, "/n", subtracting_example, "/n", multiplying_example, "/n", dividing_example)match operator:    case ("+"):        print(adding_process)    case ("-"):        print(subtracting_process)    case("*"):        print(multiplying_process)    case("x"):        print(multiplying_process)    case("x"):        print(dividing_process)