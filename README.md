Project to rextract ingredients from Filipino recipes.

Inspired from the following project: https://sites.northwestern.edu/msia/2019/05/21/chocolate-chips-and-fish-sauce-a-network-analysis-and-visualization-in-ingredient-pairings/

The following steps to retrieve ingredients are:
- Only text before a comma (if any) were filtered using regex
- A corpus of measurement terms were scraped from sites like https://www.enchantedlearning.com/wordlist/measurement.shtml and used to filter out measurement terms.
- Individual tokenized terms were tagged with nltk.pos_tag to only select adjectives and nouns.
- Plural nuns were converted to singular nouns
- If remaining ingredient had more than 2 words, only keep the last two words

