
# Easy Creation of Qualtrics Surveys for Coding (= Labeling) Text Items

This program makes it easy to create a survey for coding a set of items using Qualtrics.  You provide information about your survey in convenient file formats (plain text, which can also include HTML), and it will create a file suitable for importing into Qualtrics.

## Creating the survey file to import into Qualtrics

The input files you'll need are as follows.

| Commandline argument  | What it's for      |
| ------------------- | ------------- |
| --infile   |    Items to be coded one per line in `ID <tab> text` format |
| --introfile   |  Introduction or consent form. Must end with a Yes/No question |
| --instructionsfile   | Coding guidelines or instructions |
| --question   |    The question asked for each item (same question for all items) |


The `example` directory contains an example. You can create the example survey by executing:

```
python qualtrics_coding_survey.py \
    --infile           example/items_sample.txt \
    --introfile        example/intro.html \
    --instructionsfile example/instructions.html \
    --question         example/question.html \
    --question_footer  example/question_footer.html \
	> ./survey.txt
```

## Importing the survey file

### To create the survey in Qualtrics from scratch:

- Log in to Qualtrics and choose *Create project*, just as you would if creating a new survey by hand.

- Choose *Survey* to create a survey from scratch

- Click *Get started*

- Give your project a name, and select *Create a blank survey project*.  Click *Create Project*.

- For the default question block, click ... at upper right and *Delete*.

- Follow the Qualtrics i[nstructions on how to import a TXT survey](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/import-and-export-surveys/#ImportTXTDoc).


- Follow the instructions in `example/intro.html` to create the appropriate skip logic so that if the participant says No to the consent, it takes them to the end of the survey.

- More generally, edit the survey however you want. The hard part of creating all the questions for  your to-be-coded items has already been done for you.

### To create the survey in Qualtrics for integration with Prolific

If you will be recruiting using Prolific prolific.com , see the [Prolific Qualtrics Integration Guide](https://researcher-help.prolific.com/hc/en-gb/articles/360009224113-Qualtrics-integration-guide ) .






