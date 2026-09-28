
def write_if_statement(file, condition):
	indentation = condition[:len(condition) - len(condition.lstrip("\t"))]
	condition = condition.lstrip("\t")
	file.write(f"{indentation}if {condition}:\n")
	# file.write(f"{indentation}\tpass\n")


def write_print(file, condition):
	indentation = condition[:len(condition) - len(condition.lstrip("\t"))]
	condition = condition.lstrip("\t")
	file.write(f"{indentation}print({condition})\n")
	# file.write(f"{indentation}\tpass\n")



if __name__ == "__main__":
	try:
		range_limit = 250
		with open("calc.py", "w") as file:
			write_print(file, f"\"Welcome to the calculator!\\nPlease enter an expression with format '1 + 2' or '1 - 2'\"")
			file.write("x = input('Enter expression: ')\n")
			for i in range(0, range_limit):
				for j in range(0, range_limit):
					write_if_statement(file, f"x == '{i} + {j}'")
					write_print(file, f"\t\"result is {i + j}\"")
			for i in range(0, range_limit):
				for j in range(0, range_limit):
					write_if_statement(file, f"x == '{i} - {j}'")
					write_print(file, f"\t\"result is {i - j}\"")
	except Exception as e:
		print(f"An error occurred: {e}")
	finally:
		print("Created file")