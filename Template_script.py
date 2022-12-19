"""
Credits:
- Freek de Kreek, 2022

Description:
Lorum ipsum dolor sit amet consectetuer

Changes:
@date-of-change, description of added feature/edit

"""

# Import packages here
import argparse
import timeit

# Initialize parser, for all arguments given in command-line
parser = argparse.ArgumentParser()
# Main arguments
parser.add_argument("-i", "--Input",
                    help="Provide input file name of the distance matrix in '.xlsx' format, see help for other input "
                         "options", required=True)
parser.add_argument("-o", "--Output", help="Provide path to the output folder", required=True)

# Optional arguments
parser.add_argument("-v", "--Verbose", help="When this argument is given, it will turn on debug, this will print A LOT",
                    action="store_true")

# Variables
args = parser.parse_args()
main_input = args.Input
main_output = args.Output
verbose = args.Verbose
start = timeit.default_timer()


######################################## Functions #####################################################################

def template_function(template_input):
    """
    Put a function description here
    :param template_input:
    :return:
    """
    print(f"This is a template function with a template parameter: {template_input}")
    template_return = template_input + template_input
    return template_return


######################################## Main ##########################################################################
# Call functions here

template_caller = template_function(main_input)
with open(main_output, "x") as output_file:
    output_file.write(template_caller)

# End of script
stop = timeit.default_timer()  # ends timer
print("Finished succesfully, time taken: ", stop - start)  # prints script run duration
