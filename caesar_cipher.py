#!python3
class CaesarCipher(type):

	def __new__(self, class_name, bases, attrs):
		a = {}
		num_ordered = str(list(attrs.keys())[-1])
		associate_name = ""
		for name, value in attrs.items():
			if name.startswith("__"):
				a[name] = value
			elif name == num_ordered:
				a[associate_name] = value
			else:
				a[name] = value
			associate_name = name 
		return type(class_name, bases, a)

class Crypt(metaclass=CaesarCipher):
	ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	MAX_KEY_SIZE = len(ALPHABET)
	key = 14
	random_keys = [13, 4, 21, 4, 17, 36, 6, 14, 13, 13, 0, 36, 6, 8, 21, 4, 36, 24, 14, 20, 36, 20, 15, 36, 13, 4, 21, 4, 17, 36, 6, 14, 13, 13, 0, 36, 11, 4, 19, 36, 24, 14, 20, 36, 3, 14, 22, 13]

	def __init__(self, message):
		self.message = message
		
	def encrypt_message(self):
		encrypted_message = ''
		self.MAX_KEY_SIZE -= 1
		for symbol in self.message:
			message_char_pos =  self.ALPHABET.find(symbol)
			if message_char_pos == -1:
				encrypted_message += symbol
			else:
				encrypted_message_index = message_char_pos + self.key
				if encrypted_message_index > self.MAX_KEY_SIZE:
					encrypted_message_index -= self.MAX_KEY_SIZE
				encrypted_message += self.ALPHABET[encrypted_message_index]
		return encrypted_message  

	def decrypt_message(self):
		encrypted_message = self.message
		decrypted_message = ''
		self.MAX_KEY_SIZE -= 1
		for symbol in encrypted_message:
			symbol_index = self.ALPHABET.find(symbol)
			if symbol_index == -1:
				decrypted_message += symbol
			else:
				decrypted_message_index = symbol_index - self.key
				if decrypted_message_index < 0:
					decrypted_message_index += self.MAX_KEY_SIZE
				decrypted_message += self.ALPHABET[decrypted_message_index]
		return decrypted_message

	def DIFFERENT_CIPHER(self):
		self.message
		new_message = ''
		self.MAX_KEY_SIZE -= 1
		for symbol in self.message:
			symbol_index = self.ALPHABET.find(symbol)
			if symbol_index == -1:
				new_message += symbol
			else:
				new_cipher_index = symbol_index - self.key
				if new_cipher_index < 0:
					new_cipher_index += self.MAX_KEY_SIZE
				new_message += self.ALPHABET[new_cipher_index]
		return new_message
		
	def insert_random_keys(self):
		random_index = ""
		for i in self.random_keys:
			number = self.ALPHABET[i]
			random_index += number
		return random_index

if __name__=="__main__":
	try:
		c = Crypt
		encrypted_message = c("Hello, World! I am a programmer").encrypt_message()
		decrypted_message = c("Vszz2,Nl25zr!NWNo0NoN352u5o00s5").decrypt_message()
		#print(encrypted_message)
		print(decrypted_message)
	except:
		print("Something went wrong")