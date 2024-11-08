import numpy as np
from time import sleep

class Buf:
	def __init__(self): self._sel = [0, 0, 0]

	def queue(self, data):
		self._sel = [data, self._sel[0], self._sel[1]]

message = "011101101110010100101111"

# Generator indices
# 1, 2; 0, 2; 0, 1, 2;

codes = []

for code in range(256):
	message_1 = ""
	message_2 = ""
	message_3 = ""
	coded_message = ""
	cnt = 0
	bin_str = format(code, "08b")
	# Swap bit significance
	bin_str = bin_str[::-1]
	# Encode the data
	buf = Buf()
	for char in bin_str:
		buf.queue(int(char))
		generator_1 = buf._sel[1] ^ buf._sel[2]
		generator_2 = buf._sel[0] ^ buf._sel[2]
		generator_3 = buf._sel[0] ^ buf._sel[1] ^ buf._sel[2]
		message_1 += str(generator_1)
		message_2 += str(generator_2)
		message_3 += str(generator_3)
	# Interleave the messages
	if len(message_1) == len(message_2) and len(message_1) == len(message_3):
		for _ in range(len(message_1)):
			coded_message += message_1[_] + message_2[_] + message_3[_]
	else: raise Exception("Coded message lengths aren't matched")
	for j in range(len(coded_message)):
		if coded_message[j] != message[j]:
			cnt += 1
	codes.append([code, cnt])
for row in codes: print(row)

# 45??
