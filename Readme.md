This is the repository that contains the NLP_Assessment on "A Semi Automated Approach for Hindi Neologism" </br>

I will explain the steps that i followed to chieve this</br>

1) I collected all the News Articles in the urls.txt file</br>
2) I scraped the information from the respective urls using the web_scrapper.py that will scrapp all the required information from websites and store in data/data.csv file</br>
3) Then the collected information is manipulated and preprocessed using the preprocessing.ipynb the ipynb file contains all the required preprocessing steps and the modifeied data is stored in data/mod_data.csv file.</br>
4) then the required covid 19 corpus is extracted from the mod_data.csv file and stored in the covid_19_corpus.txt file.</br>
5) we use a lexicon/dictionary downloaded from the [IITB english-hindi dataset](https://www.cfilt.iitb.ac.in/iitb_parallel/). we use the hindi part in that.</br>
6) we next filter our corpus that will remove the common words and other unnecessary words and will focus more on the words generated after the covid 19 and this achieved by algorithm.py file and the results are stored in the filtered_corpus.txt file</br>
7) Now we come to manually work after we get the filtered_corpus we find the unique words and their counts using the unique_words.py file and the results are stored in the unique_words_and_count.txt file.

**RESULTS**</br>

1) we take 730 links we collect arucles of 730 articles randomly between 28/03/2024 to Dec/2022.</br>
2) In the filtered_corpus.txt we get nearly 49K words that are not found in the iITB english-hindi dataset.</br>
3) after that we get unique words and theri counts in the txt file there nearly 660-700 unique words that we can observe after filtering</br>
4) the top words are variants, sub variants, RT-PCR, Omicrom etc..</br>
5) in the manual filtering the process of searching on the online dictionary and then filtering was done simultaneously helping to get better results.</br>
6) the online dictionaries used are Collins (https://www.collinsdictionary.com/hi/dictionary/hindi-english) and the Oxford English-Hindi Dictionary (https://dsal.uchicago.edu/dictionaries/mcgregor/). 
