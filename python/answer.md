#chapter 1
## câu 1:

Q:1. Which of the following are operators, and which are values?
```
*

'hello'

-88.8

-

/

+

5
```

> operators: * , -, / +

> values: 'hello', -88.8 , 5

Q:2. Which of the following is a variable, and which is a string?

> spam : variable

> 'spam': string

Q:3. Name three data types.

> strings, floating-point numbers and integer.

Q: 4. What is an expression made up of? What do all expressions do?

>  expressions are just values combined with operators, and they always evaluate down to a single value

Q:5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

> an expression evaluates to a single value. A statement does not.

Q:6. What does the variable bacon contain after the following code runs?
```
bacon = 20
bacon + 1
```
> 21

Q:7. What should the following two expressions evaluate to?
```
'spam' + 'spamspam'
'spam' * 3
```
> spamspamspams

> pamspamspam

Q:8. Why is eggs a valid variable name while 100 is invalid?

> because '100' begins with number


Q:9. What three functions can be used to get the integer, floating-point number, or string version of a value?
> str(), int(), float()

Q:10. Why does this expression cause an error? How can you fix it?
```
'I have eaten ' + 99 + ' burritos.'
```
> The expression causes an error because 99 is an integer, and only strings can be concatenated to other strings with the + operator. The correct way is I have eaten ' + str(99) + ' burritos.'.

# Chapter 2
Q:1. What are the two values of the Boolean data type? How do you write them?
> True and False

>
Q:2. What are the three Boolean operators?

Q:3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
>

Q:4. What do the following expressions evaluate to?
```
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```
> False

> False

> True

> False

> True

Q:5. What are the six comparison operators?

```

== Equal to

!= Not equal to

< Less than

> Greater than

<= Less than or equal to

>= Greater than or equal to
```

Q:6. What is the difference between the equal to operator and the assignment operator?
>

Q:7. Explain what a condition is and where you would use one.
>

Q:8. Identify the three blocks in this code:
```
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```
>  

Q:9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

Q:10. What can you press if your program is stuck in an infinite loop?

Q:11. What is the difference between break and continue?

Q:12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

Q:13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Q:14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

**Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.**
