#User inputs numbers for how much Bread, Peanut Butter, and Jelly they have.
bread = int(raw_input("How many slices of bread do you have?"))
pb = int(raw_input("How many tablespoons of peanut butter do you have?"))
jelly = int(raw_input("How many tablespoons of jelly do you have?"))

#Check if Bread > 0
if bread > 0:
	#Check if Bread is even
	if bread % 2 == 0:
		#Check if there is peanut butter
		if pb > 0:
			#Check if there is jelly
			if jelly > 0:
				#Check if Bread/2 is smallest
				if bread / 2 < jelly and bread / 2 < pb:
					#Tell user they can make sandwiches = bread/2.
					print "You can make {0} peanut butter and jelly sandwiches.".format(bread / 2)
				#Check if Jelly is largest
				elif jelly < bread / 2 and jelly < pb:
					#Tell user they can make sandwiches = jelly.
					print "You can make {0} peanut butter and jelly sandwiches.".format(jelly)
				else:
					#Tell user they can make sandwiches = pb.
					print "You can make {0} peanut butter and jelly sandwiches.".format(pb)
			else:
				#Check if bread is largest
				if bread / 2 < pb:
					print "You can make {0} peanut butter sandwiches, but isn't that a bit dry?".format(bread / 2)
				else:
					print "You can make {0} peanut butter sandwiches, but isn't that a bit dry?".format(pb)
		else:
			#Check if Jelly > 0
			if jelly > 0:
				#Check if Bread/2 < Jelly
				if bread / 2 < jelly:
					#Tell user they can make sandwiches = Bread/2
					print "You can make {0} jelly sandwiches, but isn't that a bit sweet? You need peanut butter for the perfect sandwich.".format(bread / 2)
				else:
					#Tell user they can make sandwiches = Jelly
					print "You can make {0} jelly sandwiches, but isn't that a bit sweet? You need peanut butter for the perfect sandwich.".format(jelly)
			else:
				#Tell user they need toppings for a sandwich.
				print "You just have bread. For a great sandwich, you need to get yourself some peanut butter and jelly. You need at least one tablespoon of each."
	else:
		#Check if there is peanut butter
		if pb > 0:
			#Check if there is jelly
			if jelly > 0:
				#Check if Bread is smallest
				if bread < jelly and bread < pb:
					#Tell user they can make sandwiches = bread.
					print "You can make {0} open-faced peanut butter and jelly sandwiches.".format(bread)
				#Check if Jelly is smallest
				elif jelly < bread and jelly < pb:
					#Tell user they can make sandwiches = jelly.
					print "You can make {0} open-faced peanut butter and jelly sandwiches.".format(jelly)
				else:
					#Tell user they can make sandwiches = pb.
					print "You can make {0} open-faced peanut butter and jelly sandwiches.".format(pb)
			else:
				#Check if bread is smallest
				if bread < pb:
					print "You can make {0} open-faced peanut butter sandwiches, but isn't that a bit dry?".format(bread)
				else:
					print "You can make {0} open-faced peanut butter sandwiches, but isn't that a bit dry?".format(pb)
		else:
			#Check if Jelly > 0
			if jelly > 0:
				#Check if Bread > Jelly
				if bread > jelly:
					#Tell user they can make sandwiches = Bread/2
					print "You can make {0} open-faced jelly sandwiches, but isn't that a bit sweet? You need peanut butter for the perfect sandwich.".format(bread)
				else:
					#Tell user they can make sandwiches = Jelly
					print "You can make {0} open-faced jelly sandwiches, but isn't that a bit sweet? You need peanut butter for the perfect sandwich.".format(jelly)
			else:
				#Tell user they need toppings for a sandwich.
				print "You just have bread. For a great sandwich, you need to get yourself some peanut butter and jelly. You need at least one tablespoon of each."
else:
	#Check if there's peanut butter
	if pb > 0:
		#Check if there's jelly
		if jelly > 0:
			#Tell user they need bread.
			print "You have peanut butter and jelly, but you need bread to make a sandwich."
		else:
			#Tell user they need bread and jelly
			print "You have peanut butter. You need bread and jelly to make a peanut butter and jelly sandwich. If you want a peanut butter sandwich, you still need bread."
	else:
		#Check if there's jelly
		if jelly > 0:
			print "You have jelly. You need bread and peanut butterto make a peanut butter and jelly sandwich. If you want a jelly sandwich, you still need bread."
		else:
			print "You don't have any ingredients. You need bread, peanut butter, and jelly to make a peanut butter and jelly sandwich.\nYou need peanut butter and bread for a peanut butter sandwich.\nYou need jelly and bread for a jelly sandwich."
