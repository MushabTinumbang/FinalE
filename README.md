# FinalE
Prime Minister has announced that the government will give financial aid to reduce the burden of the
people during the pandemic. Upon this initiation, recipient will receive money with the following
amounts:
• RM1000 for household category B40
• RM600 for household category M40
In this problem, 𝑁 data are given which contains the category, name, and the amount of money
received. You are asked to display all data in a category, B40 or M40. Output the information of the
recipients in that category, how many recipients are in that category, and the total amount of money
for all of the recipients in that category.

First, for all recipients under the asked category, output the category, name, and the amount of money
received. Print in the order from the input.
In the next line, output “Total Recipients: ”, followed by the number of recipients under the asked
category.
In the next line, output “Total Amount: “, followed by the total amount of money for all recipients
under the category.

Constraints
• 1 ≤ 𝑁 ≤ 50
• Length of name is between 1 and 20 (inclusive). Names consist of upper case Latin alphabet.
• Category can only be B40 or M40.
• It is guaranteed that the amount of money received is in accordance with the category and the
provisions that hae been explained in the description above.

Sample Input 
6
B40,Sofea,1000
M40,Mikael,600
B40,Adam,1000
B40,Irene,1000
M40,Cyntia,600
B40,Alif,1000
B40

Sample Output

B40 Sofea 1000
B40 Adam 1000
B40 Irene 1000
B40 Alif 1000
Total Recipients: 4
Total Amount: 4000
