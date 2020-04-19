# 25	Strings	Write a program to print the different data types (Numbers, strings characters) using the Format symbols (Refer to different format symbols specified in Tutorial)

# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format


# :<		Left aligns the result (within the available space)
print("we have {:<8} Employees '<' to left-align the value".format(100))
# :>		Right aligns the result (within the available space)
print("We are total {:>8} students in the class '>' to right-align the value".format(20))
# :^		Center aligns the result (within the available space)
print("We are total {:^8} students in the class".format(20))
# :=		Places the sign to the left most position
print("Todays temperature is  {:=6} degree".format(-5))
print("We are total {:n} students in the class ".format(50))
print("We are total {:.0%} students in the class ".format(.25))