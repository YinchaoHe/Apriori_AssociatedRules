# Apriori_AssociatedRules
Get the associated rules from 1984 United States Congressional Voting Records Database using Apriori algorithm.

## Description 
- csce474_apriori.py is used to determine the frequent sets in a dataset and then generate the association rules, the inputs are minimum support and minimum confidence. In addition,  the outputs are graphs that plot the runtime of the algorithm and the number of rules generated as a function of minimum support, and a .txt file that has all association rules of the dataset. (Mention: the user only needs to input minimum support and minimum confidence once, then the program will run the algorithm ten times, every time minimum support increases 0.1)
- ioprocess.py is used to convert .csv file into the matrix, create the graph and write out the association rules to a .txt file.
- rulenumber.csv is one of the output files, that record the number of rules generated as a function of minimum support.
-runtime.csv is one of the output files, that record the runtime of the algorithm generated as a function of minimum support.
- asso_rule.txt is one of the output files, that record the association rules generated as a function of minimum support.
- vote.csv is an input file, that is the dataset of this program.

## Usage:
- Running the module in the terminal:
  * `python3 csce474_apriori.py -s [minimum support] -c [minimum confidence]`\ 
  (example: python3 csce474_apriori.py -s 0.1 -c 1)

 




