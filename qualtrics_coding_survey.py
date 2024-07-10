################################################################
#
# Easy creation of a survey in the Qualtrics text import format.
# For info on how to import the survey created by this program, see
# https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/import-and-export-surveys/#ImportTXTDoc
#
# Arguments:
#
#   --infile INFILE                       TSV/TXT file: ID <tab> text
#   --introfile INTROFILE                 HTML file with consent/intro
#   --instructionsfile INSTRUCTIONSFILE   HTML file with instructions
#   --question QUESTION                   HTML file with per-item question
#   --mcoptions MCOPTIONS                 Multiple choice options (default: Yes,No)
#   -h, --help                            show this help message and exit
#
#  Note that the survey this creates does not contain any
#  flow logic; notably, a "no" to the intro/consent
#  does not take you to the end of the survey.
#
################################################################
import csv
import sys
import argparse

# Copies a file to stdout
def read_and_output_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

def generate_mc_choices(optionslist):
    print("[[AdvancedChoices]]")
    for option in optionslist:
        print("[[Choice]]")
        print(option)
    print("\n")

def generate_pagebreak():
    print("\n[[PageBreak]]\n")
        
# Generates intro section of survey (e.g. consent)
# Intro must end in a yes/no question, e.g.
# Do you want to continue? or Do you agree?
def generate_intro(introfile):
    print("[[AdvancedFormat]]",
          "[[ED:SawSurvey:1]]",
          "[[Block:Intro]]",
          "[[Question:MC:SingleAnswer]]",
          sep='\n')
    read_and_output_file(introfile)
    generate_mc_choices(['Yes','No'])

# Generates instructions section of survey (e.g. consent)
# Instructions must end in a yes/no question, e.g.
# Do you want to continue? Do you agree?
def generate_instructions(instructionsfile):
    print("\n",
          "[[Block:Instructions]]",
          "[[Question:MC:SingleAnswer]]",
          sep='\n')
    read_and_output_file(instructionsfile)
    
def generate_questions(infile, question, options):
    # print(f"DEBUG: infile = {infile}")
    # print(f"DEBUG: question = {question}")
    print("[[Block:Items]]")
    with open(args.infile, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            item_id = row[0]
            item    = row[1]
            # print(f"DEBUG: item_id = {item_id}")
            # print(f"DEBUG: item = {item}")
            # print(f"DEBUG: options = {options}")
            print("[[Question:MC:SingleAnswer]]",
                  f"{item}",
                  "<p>&nbsp;</p>",
                  question,
                  sep='\n')
            print(f"[[ID:{item_id}]]")
            generate_mc_choices(options)
            print("[[PageBreak]]")
            print("\n")

if __name__ == '__main__':
    
    # Handle command line
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile',   dest='infile', default=None,
                        help='TSV/TXT file:  ID <tab> text')
    parser.add_argument('--introfile',   dest='introfile', default=None,
                        help='HTML file with consent/intro')
    parser.add_argument('--instructionsfile',   dest='instructionsfile', default=None,
                        help='HTML file with instructions')
    parser.add_argument('--question',   dest='question', default=None,
                        help='HTML file with per-item question')
    parser.add_argument('--mcoptions',   dest='mcoptions', default="Yes,No",
                        help='Multiple choice options (default: Yes,No)')

    args    = parser.parse_args()
    argdict = args.__dict__
    if None in list(argdict.values()):
        print("Missing an argument. Use --help to see usage")
        sys.exit(1)

    # Generate the sections of the survey
        
    generate_intro(args.introfile)

    generate_pagebreak()

    generate_instructions(args.instructionsfile)

    generate_pagebreak()

    # print(f"DEBUG: reading question from {args.question}")
    with open(args.question, 'r') as f:
        question = f.read()
    generate_questions(args.infile, question, args.mcoptions.split(','))

