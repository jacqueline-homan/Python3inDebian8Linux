secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 3

while pw != secret:
	count += 1
	if count > max_attempt: break
	pw = input(f"{count}: What is the secret password?")
	else:
		auth = True
print("Authorized" if auth else "Calling the FBI...")

#if __name__ == "__main__": main()