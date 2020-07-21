# Recipe ingredient extraction

The objective is to create a data collection service that the user can use to copy and paste text of the recipe to extract the ingredients from the text. 

![sequence diagram](/docs/sequence_diagram.png)

## Front-end and API for user interaction

The service will consist of a simple front-end where the use can copy and paste the recipe name, ingredients and source website and send the text to an API for processing. The API will then return the processed text to the user.

## Extracting the ingredients

Inspired from the following project: https://sites.northwestern.edu/msia/2019/05/21/chocolate-chips-and-fish-sauce-a-network-analysis-and-visualization-in-ingredient-pairings/

The following steps to retrieve ingredients are:
- Only text before a comma (if any) were filtered using regex
- A corpus of measurement terms were scraped from sites like https://www.enchantedlearning.com/wordlist/measurement.shtml and used to filter out measurement terms.
- Individual tokenized terms were tagged with nltk.pos_tag to only select adjectives and nouns.
- Plural nuns were converted to singular nouns
- If remaining ingredient had more than 2 words, only keep the last two words

References
- https://www.frontiersin.org/articles/10.3389/fict.2017.00014/full

### TODOs
- Probably need to convert the NLP logic to client JS code
- Begin writing API