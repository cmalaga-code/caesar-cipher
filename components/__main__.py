import art

def ceaser(input_text, shift_number, alphabet, encrypt):
	text = ""
	for char in input_text:
		if char in alphabet:
			index_alphabet = alphabet.index(char)
			if encrypt:
				text += alphabet[index_alphabet + shift_number]
			else:
				text += alphabet[index_alphabet - shift_number]
		else:
			text += char
	return text


if __name__ == "__main__":
	print(art.logo)
	loop = True
	while loop:
		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
		text = input("Type your message:\n").lower()
		shift = int(input("Type the shift number:\n"))
	
		if direction == "encode":
			if shift % 26 != 0:
				shift = shift % 26
			encrypted_text = ceaser(text, shift, alphabet, True)
			print(f"Results: {encrypted_text}")
		else:
			if shift % 26 != 0:
				shift = shift % 26
			decrypt_text = ceaser(text, shift, alphabet, False)
			print(f"Results: {decrypt_text}")
		user_continue = input("Do you want to continue ? type 'yes' or 'no'\n")
		if user_continue == "no":
			loop = False
		
	
