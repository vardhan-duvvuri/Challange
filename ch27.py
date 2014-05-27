def RiskGame(attacker, defender):
	attack = sorted(attacker)
	defend = sorted(defender)
	count1 = 0
	count2 = 0
	i = 0
	while i < 2:
		k = attack.pop()
		l = defend.pop()

		if k > l:
			count1+=1
		else:
			count2+=1

		i+=1

	if count1 == 2:
		return 'Defender loses 2 armies.'
	elif count2 == 2:
		return 'Attacker loses 2 armies.'
	else:
		return 'Attacker loses 1 army and defender loses 1 army.'

if __name__ == "__main__":
	print RiskGame([1,4,1], [1, 2])
