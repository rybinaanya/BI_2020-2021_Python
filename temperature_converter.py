# Hello message, short instructions
message = 'Hello! This is a temperature unit converter.\n' \
          'It supports Celsius (C), Fahrenheit (F), ' \
          'Kelvin (K), Rankine (Ra) and Réaumur (Re) units.'
print(message)


# Create a function that converts temperature from one scale to another.
# Function takes 3 variable: input temperature
# value (temp_value_in_), input and output temperature units
# (unit_i and unit_o, respectively). Returns temperature
# value in desired scale.
def temp_convert(temp_value_in_, unit_i, unit_o):
    temp_value_out_ = 0
    if unit_i == 'C':
        if unit_o == 'F':
            temp_value_out_ = temp_value_in_ * 9 / 5 + 32
        elif unit_o == 'K':
            temp_value_out_ = temp_value_in_ + 273.15
        elif unit_o == 'Ra':
            temp_value_out_ = (temp_value_in_ + 273.15) * 9 / 5
        elif unit_o == 'Re':
            temp_value_out_ = temp_value_in_ * 4 / 5
        else:
            print('Error: output temperature unit should be a capital letter.'
                  'The program accepts the following units: C, F, K, Re, Ra')
    elif unit_i == 'F':
        if unit_o == 'C':
            temp_value_out_ = (temp_value_in_ - 32) * 5 / 9
        elif unit_o == 'K':
            temp_value_out_ = (temp_value_in_ + 459.67) * 5 / 9
        elif unit_o == 'Ra':
            temp_value_out_ = temp_value_in_ + 459.67
        elif unit_o == 'Re':
            temp_value_out_ = (temp_value_in_ - 32) * 4 / 9
        else:
            print('Error: output temperature unit should be a capital letter. '
                  'The program accepts the following units: C, F, K, Re, Ra')
    elif unit_i == 'K':
        if unit_o == 'F':
            temp_value_out_ = temp_value_in_ * 9 / 5 - 459.67
        elif unit_o == 'C':
            temp_value_out_ = temp_value_in_ - 273.15
        elif unit_o == 'Ra':
            temp_value_out_ = temp_value_in_ * 9 / 5
        elif unit_o == 'Re':
            temp_value_out_ = (temp_value_in_ - 273.15) * 4 / 5
        else:
            print('Error: output temperature unit should be a capital letter. '
                  'The program accepts the following units: C, F, K, Re, Ra')
    elif unit_i == 'Ra':
        if unit_o == 'F':
            temp_value_out_ = temp_value_in_ - 459.67
        elif unit_o == 'K':
            temp_value_out_ = temp_value_in_ * 5 / 9
        elif unit_o == 'C':
            temp_value_out_ = (temp_value_in_ - 491.67) * 5 / 9
        elif unit_o == 'Re':
            temp_value_out_ = (temp_value_in_ - 491.67) * 4 / 9
        else:
            print('Error: output temperature unit should be a capital letter. '
                  'The program accepts the following units: C, F, K, Re, Ra')
    elif unit_i == 'Re':
        if unit_o == 'F':
            temp_value_out_ = temp_value_in_ * 9 / 4 + 32
        elif unit_o == 'K':
            temp_value_out_ = temp_value_in_ * 5 / 4 + 273.15
        elif unit_o == 'Ra':
            temp_value_out_ = temp_value_in_ * 9 / 4 + 491.67
        elif unit_o == 'C':
            temp_value_out_ = temp_value_in_ * 5 / 4
        else:
            print('Error: output temperature unit should be a capital letter. '
                  'The program accepts the following units: C, F, K, Re, Ra')
    else:
        print('Error: input temperature unit should be a capital letter. '
              'The program accepts the following units: C, F, K, Re, Ra')
    return temp_value_out_


# Create dictionaries needed for checking the entered values
dict_abs_zeroes = {'C': -273.15, 'F': -459.67, 'K': 0.00,
                   'Ra': 0.00, 'Re': -218.52}
dict_unit_name = {'C': 'Celsius', 'F': 'Fahrenheit', 'K': 'Kelvin',
                  'Ra': 'Rankine', 'Re': 'Réaumur'}

# Enter values and check them using created dictionary
# Specify input unit:
unit_in = input('Enter an input unit (eg.  C, F, K, Ra, Re): ')

# Check the correctness of the input unit:
if unit_in in dict_abs_zeroes:
    try:
        # Specify temperature value:
        temp_value_in = float(input('Enter a temperature value: '))
        input_abs_zero = dict_abs_zeroes[unit_in]
        input_scale = dict_unit_name[unit_in]

        # Temperature value should be not less than absolute zero
        # in a corresponding temperature scale:
        if temp_value_in >= input_abs_zero:
            # Specify temperature value:
            unit_out = input('Enter an output unit (eg.  C, F, K, Ra, Re): ')

            if unit_out in dict_abs_zeroes:
                # Convert temperature using function temp_convert:
                temp_value_out = temp_convert(temp_value_in, unit_in, unit_out)

                # Keep 4 decimal places
                temp_value_in = float('{:.4f}'.format(temp_value_in))
                temp_value_out = float('{:.4f}'.format(temp_value_out))

                # Print an answer:
                print('Temperature of ' + str(temp_value_in) + ' '
                      + input_scale + ' degree is equal to '
                      + str(temp_value_out) + ' '
                      + dict_unit_name[unit_out] +
                      ' degree.')
            else:
                print('Output temperature unit should be a capital letter. '
                      'The program accepts the following units: '
                      'C, F, K, Re, Ra')
        else:
            abs_zero_error_message = 'Error: temperature value must be ' \
                                     'not less than ' \
                                     'absolute zero which is ' \
                                     + str(input_abs_zero) + \
                                     ' degree for the ' \
                                     + input_scale + ' scale!'

            print(abs_zero_error_message)
    except ValueError:
        print('Error: entered temperature value should be a number')
else:
    print('Input temperature unit should be a capital letter. '
          'The program accepts the following units: C, F, K, Re, Ra')
